"""Run the real native entry point with inert tools to prove security failures block."""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class WorkflowSecurity(unittest.TestCase):
    def invoke(self, failed=None):
        launcher = shutil.which("bash")
        self.assertIsNotNone(launcher)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            binary = root / "bin"
            binary.mkdir()
            log = root / "calls.jsonl"
            for name in ["markdownlint-cli2", "shellcheck", "ruff", "python3", "bash", "actionlint", "zizmor"]:
                path = binary / name
                path.write_text("#!" + sys.executable + "\nimport json,os,sys\nfrom pathlib import Path\np=Path(os.environ['CALL_LOG'])\nwith p.open('a') as out: out.write(json.dumps([Path(sys.argv[0]).name,*sys.argv[1:]])+'\\n')\nsys.exit(17 if Path(sys.argv[0]).name==os.environ.get('FAILED_TOOL') else 0)\n")
                path.chmod(0o755)
            environment = dict(os.environ, PATH=str(binary) + ":/usr/bin:/bin", CALL_LOG=str(log), FAILED_TOOL=failed or "")
            result = subprocess.run([launcher, str(ROOT / "scripts/check-development.sh")], env=environment, capture_output=True, text=True, check=False)
            calls = [json.loads(line) for line in log.read_text().splitlines()]
            return result, [row for row in calls if row[0] in {"actionlint", "zizmor"}]

    def test_native_entrypoint_requires_both_exact_security_commands(self):
        result, calls = self.invoke()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(calls, [["actionlint"], ["zizmor", "--offline", "--min-severity", "medium", "--min-confidence", "medium", ".github"]])

    def test_each_security_failure_propagates(self):
        for tool in ["actionlint", "zizmor"]:
            with self.subTest(tool=tool):
                result, calls = self.invoke(tool)
                self.assertEqual(result.returncode, 17, result.stderr)
                if tool == "actionlint":
                    self.assertEqual(calls, [["actionlint"]])
                else:
                    self.assertEqual(calls[-1][0], "zizmor")


if __name__ == "__main__":
    unittest.main()
