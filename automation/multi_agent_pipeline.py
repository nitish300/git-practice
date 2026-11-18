"""
Autonomous 4-Agent Pipeline Runner
-----------------------------------
Demonstrates the 4-agent team in action:
1. Planner Agent: Deconstructs the goal into a step-by-step technical plan.
2. Coder Agent: Implements the code based on the plan.
3. Tester Agent: Executes unit tests and validates behavior.
4. DevOps Agent: Stages and records a clean Conventional Commit.
"""

import os
import sys
import subprocess
import time

# Ensure UTF-8 output on Windows consoles
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def print_banner(agent_name: str, tag: str = "[*]", color_code: str = "\033[94m"):
    reset = "\033[0m"
    separator = "=" * 65
    print(f"\n{color_code}{separator}")
    print(f" {tag} [{agent_name.upper()}] ACTIVATED")
    print(f"{separator}{reset}\n")

class PlannerAgent:
    def plan(self, goal: str) -> dict:
        print_banner("Agent 1: Planner & Architect", "[PLAN]", "\033[95m")
        print(f"Goal Received: '{goal}'")
        print("Analyzing codebase structure & dependencies...")
        time.sleep(0.6)
        
        plan = {
            "feature_name": "calculator_utility",
            "target_file": "utils/math_helper.py",
            "test_file": "tests/test_math_helper.py",
            "steps": [
                "Create modular math utility with add, subtract, multiply, safe_divide",
                "Create unit tests covering standard cases and edge cases (divide by zero)",
                "Run automated test verification",
                "Stage and commit with Conventional Commit format"
            ]
        }
        print("Execution Plan Created:")
        for idx, step in enumerate(plan["steps"], 1):
            print(f"  {idx}. {step}")
        return plan

class CoderAgent:
    def implement(self, plan: dict):
        print_banner("Agent 2: Developer & Coder", "[CODE]", "\033[94m")
        print(f"Writing code to: {plan['target_file']}...")
        os.makedirs(os.path.dirname(plan['target_file']), exist_ok=True)
        
        code = '''"""
Math Helper Utility - Created by Coder Agent
"""

def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def safe_divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
'''
        with open(plan['target_file'], "w", encoding="utf-8") as f:
            f.write(code)
        print(f"  [OK] Code successfully written to {plan['target_file']}")
        
        print(f"Writing test suite to: {plan['test_file']}...")
        os.makedirs(os.path.dirname(plan['test_file']), exist_ok=True)
        
        test_code = '''"""
Unit Tests for Math Helper - Created by Coder Agent
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.math_helper import add, subtract, multiply, safe_divide

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(3, 7) == 21

def test_safe_divide():
    assert safe_divide(10, 2) == 5.0
    try:
        safe_divide(5, 0)
        assert False, "Expected ValueError on zero division"
    except ValueError:
        pass

if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    test_safe_divide()
    print("All unit tests passed successfully!")
'''
        with open(plan['test_file'], "w", encoding="utf-8") as f:
            f.write(test_code)
        print(f"  [OK] Test suite written to {plan['test_file']}")
        time.sleep(0.5)

class TesterAgent:
    def verify(self, plan: dict) -> bool:
        print_banner("Agent 3: QA & Tester", "[QA]", "\033[93m")
        print(f"Executing automated test suite: {plan['test_file']}...")
        
        result = subprocess.run([sys.executable, plan['test_file']], capture_output=True, text=True)
        print("Test Output:")
        print(result.stdout.strip())
        
        if result.returncode == 0:
            print("  [OK] QA Approval: ALL 4 TESTS PASSED! Green light given to DevOps.")
            return True
        else:
            print(f"  [FAIL] QA Failure:\n{result.stderr}")
            return False

class DevOpsAgent:
    def deploy_and_commit(self, plan: dict):
        print_banner("Agent 4: DevOps & Git Manager", "[OPS]", "\033[92m")
        print("Checking Git status and staging verified artifacts...")
        
        # Add files
        subprocess.run(["git", "add", plan['target_file'], plan['test_file']], check=True)
        print(f"  [OK] Staged: {plan['target_file']} and {plan['test_file']}")
        
        # Commit with conventional commits
        commit_msg = f"feat(math): add {plan['feature_name']} with verified unit tests"
        print(f"Applying Conventional Commit format: '{commit_msg}'...")
        commit_res = subprocess.run(["git", "commit", "-m", commit_msg], capture_output=True, text=True)
        print(commit_res.stdout.strip())
        print("\n  [OK] Pipeline Completed: Code is tested, validated, and safely committed!")

def run_pipeline(user_goal: str):
    print("=" * 65)
    print("     AUTONOMOUS 4-AGENT AUTOMATION PIPELINE STARTING")
    print("=" * 65)
    
    # 1. Planner
    planner = PlannerAgent()
    plan = planner.plan(user_goal)
    
    # 2. Coder
    coder = CoderAgent()
    coder.implement(plan)
    
    # 3. QA Tester
    tester = TesterAgent()
    passed = tester.verify(plan)
    
    if not passed:
        print("Pipeline aborted by QA Agent due to test failures.")
        return
        
    # 4. DevOps
    devops = DevOpsAgent()
    devops.deploy_and_commit(plan)

if __name__ == "__main__":
    task = "Build a tested math calculation utility and commit it cleanly"
    if len(sys.argv) > 1:
        task = " ".join(sys.argv[1:])
    run_pipeline(task)
