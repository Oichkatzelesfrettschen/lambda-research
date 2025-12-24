#!/usr/bin/env python3
"""
orchestrator.py

Copyright (C) 2025 Lambda Research Collective

This file is part of Lambda Calculus Research Repository.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""


"""
Task Orchestrator - Automated Implementation System
Executes IMPLEMENTATION_ROADMAP.md using agents and automation
"""

import json
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import List, Optional, Dict, Any

class TaskStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    BLOCKED = "blocked"
    COMPLETE = "complete"
    FAILED = "failed"

class TaskPriority(Enum):
    CRITICAL = "[CRITICAL]"
    HIGH = "[HIGH]"
    MEDIUM = "[MEDIUM]"
    LOW = "[LOW]"

@dataclass
class Task:
    id: str
    name: str
    phase: int
    owner: str  # Agent name or "manual"
    priority: TaskPriority
    estimated_hours: float
    status: TaskStatus
    dependencies: List[str]
    success_criteria: List[str]
    commands: List[str]
    validation: List[str]
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "phase": self.phase,
            "owner": self.owner,
            "priority": self.priority.value,
            "estimated_hours": self.estimated_hours,
            "status": self.status.value,
            "dependencies": self.dependencies,
            "success_criteria": self.success_criteria,
            "commands": self.commands,
            "validation": self.validation,
        }

class TaskOrchestrator:
    """Orchestrates task execution across agents and manual steps"""
    
    def __init__(self, repo_path: Path):
        self.repo_path = repo_path
        self.admin_path = repo_path / "admin"
        self.tasks_file = self.admin_path / "tasks.json"
        self.progress_file = self.admin_path / "progress.json"
        self.tasks: Dict[str, Task] = {}
        self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from IMPLEMENTATION_ROADMAP.md or tasks.json"""
        if self.tasks_file.exists():
            with open(self.tasks_file) as f:
                data = json.load(f)
                for task_data in data["tasks"]:
                    task = Task(
                        id=task_data["id"],
                        name=task_data["name"],
                        phase=task_data["phase"],
                        owner=task_data["owner"],
                        priority=TaskPriority(task_data["priority"]),
                        estimated_hours=task_data["estimated_hours"],
                        status=TaskStatus(task_data["status"]),
                        dependencies=task_data["dependencies"],
                        success_criteria=task_data["success_criteria"],
                        commands=task_data["commands"],
                        validation=task_data["validation"],
                    )
                    self.tasks[task.id] = task
        else:
            self.initialize_tasks_from_roadmap()
            self.save_tasks()
    
    def initialize_tasks_from_roadmap(self):
        """Initialize task database from IMPLEMENTATION_ROADMAP.md"""
        # Phase 1 Tasks
        self.tasks = {
            "1.1": Task(
                id="1.1",
                name="Complete Git Migration",
                phase=1,
                owner="manual",
                priority=TaskPriority.CRITICAL,
                estimated_hours=0.5,
                status=TaskStatus.PENDING,
                dependencies=[],
                success_criteria=[
                    "git status --short | wc -l returns 0",
                    "All untracked files committed",
                    "Remote repository updated",
                ],
                commands=[
                    "git add docs/ admin/ *.md scripts/",
                    "git commit -m 'feat: complete thematic restructuring'",
                    "git push origin master",
                ],
                validation=[
                    "git status --short",
                    "git log -1 --oneline",
                ],
            ),
            "1.2.1": Task(
                id="1.2.1",
                name="Delete Abandoned Virtual Environment",
                phase=1,
                owner="manual",
                priority=TaskPriority.HIGH,
                estimated_hours=0.17,
                status=TaskStatus.PENDING,
                dependencies=["1.1"],
                success_criteria=[
                    ".audit-venv/ directory removed",
                    "Repository size reduced",
                ],
                commands=[
                    "rm -rf .audit-venv",
                    "du -sh venv/ uss-venv/",
                ],
                validation=[
                    "test ! -d .audit-venv",
                    "du -sh .",
                ],
            ),
            "1.2.2": Task(
                id="1.2.2",
                name="USS Decision - Extract or Make Optional",
                phase=1,
                owner="consolidation-architect",
                priority=TaskPriority.HIGH,
                estimated_hours=1.5,
                status=TaskStatus.PENDING,
                dependencies=["1.2.1"],
                success_criteria=[
                    "USS extracted to separate repo OR made optional",
                    "Repository size < 2GB",
                    "Decision documented",
                ],
                commands=[],  # Agent decides
                validation=[
                    "du -sh . | awk '{print $1}'",
                    "test -f experiments/README.md || test -f requirements-science-optional.txt",
                ],
            ),
            "1.3.1": Task(
                id="1.3.1",
                name="Update CLAUDE.md Implementation Strategy",
                phase=1,
                owner="documentation-architect",
                priority=TaskPriority.HIGH,
                estimated_hours=1.0,
                status=TaskStatus.PENDING,
                dependencies=["1.1"],
                success_criteria=[
                    "No references to 'external implementations'",
                    "Internal Rust workspace documented",
                    "Build instructions accurate",
                ],
                commands=[],  # Agent task
                validation=[
                    "grep -L 'external implementations' CLAUDE.md",
                    "grep 'tapl-rust' CLAUDE.md",
                ],
            ),
            "1.3.2": Task(
                id="1.3.2",
                name="Create Rust Implementation Guide",
                phase=1,
                owner="documentation-architect",
                priority=TaskPriority.HIGH,
                estimated_hours=1.0,
                status=TaskStatus.PENDING,
                dependencies=["1.3.1"],
                success_criteria=[
                    "docs/implementations/rust/README.md exists",
                    "Guide explains workspace structure",
                    "Build instructions tested",
                ],
                commands=[],  # Agent task
                validation=[
                    "test -f docs/implementations/rust/README.md",
                    "cd sources/rust-implementations/tapl-rust && cargo build",
                ],
            ),
            "1.4": Task(
                id="1.4",
                name="Fix or Remove Broken MkDocs Config",
                phase=1,
                owner="documentation-architect",
                priority=TaskPriority.MEDIUM,
                estimated_hours=1.0,
                status=TaskStatus.PENDING,
                dependencies=["1.1"],
                success_criteria=[
                    "Either simplified config deleted OR both configs work",
                    "No broken links in navigation",
                ],
                commands=[],  # Agent decides
                validation=[
                    "mkdocs build --strict",
                ],
            ),
            "1.5": Task(
                id="1.5",
                name="Restore and Run Validation",
                phase=1,
                owner="integration-test",
                priority=TaskPriority.MEDIUM,
                estimated_hours=0.5,
                status=TaskStatus.PENDING,
                dependencies=["1.1", "1.3.1"],
                success_criteria=[
                    "Validation script runs without errors",
                    "Baseline report generated",
                ],
                commands=[],  # Agent task
                validation=[
                    "python3 scripts/validate-repository.py",
                    "test -f validation_report.json",
                ],
            ),
        }
        
        # Phase 2 and 3 tasks would be added similarly...
    
    def save_tasks(self):
        """Save current task state to JSON"""
        data = {
            "last_updated": datetime.now().isoformat(),
            "tasks": [task.to_dict() for task in self.tasks.values()],
        }
        self.tasks_file.parent.mkdir(exist_ok=True)
        with open(self.tasks_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def get_ready_tasks(self) -> List[Task]:
        """Get tasks that are ready to execute (dependencies met)"""
        ready = []
        for task in self.tasks.values():
            if task.status == TaskStatus.PENDING:
                deps_met = all(
                    self.tasks[dep].status == TaskStatus.COMPLETE
                    for dep in task.dependencies
                    if dep in self.tasks
                )
                if deps_met:
                    ready.append(task)
        return sorted(ready, key=lambda t: (t.phase, -t.priority.value.count("[CRITICAL]")))
    
    def execute_task(self, task_id: str) -> bool:
        """Execute a single task"""
        task = self.tasks[task_id]
        print(f"\n{'='*70}")
        print(f"Executing Task {task.id}: {task.name}")
        print(f"Phase: {task.phase} | Owner: {task.owner} | Priority: {task.priority.value}")
        print(f"Estimated: {task.estimated_hours} hours")
        print(f"{'='*70}\n")
        
        task.status = TaskStatus.IN_PROGRESS
        self.save_tasks()
        
        try:
            if task.owner == "manual":
                return self.execute_manual_task(task)
            else:
                return self.execute_agent_task(task)
        except Exception as e:
            print(f"[FAIL] Task {task.id} failed: {e}")
            task.status = TaskStatus.FAILED
            self.save_tasks()
            return False
    
    def execute_manual_task(self, task: Task) -> bool:
        """Execute a manual task with user confirmation"""
        print(f"[TASKS] Manual task requiring your action:\n")
        print(f"Commands to execute:")
        for cmd in task.commands:
            print(f"  $ {cmd}")
        print(f"\nSuccess criteria:")
        for criterion in task.success_criteria:
            print(f"  [ ] {criterion}")
        
        response = input("\n Execute these commands? [y/N/s(kip)]: ").lower()
        
        if response == 's':
            task.status = TaskStatus.PENDING
            self.save_tasks()
            return False
        elif response != 'y':
            print("[PENDING]  Task skipped by user")
            return False
        
        # Execute commands
        for cmd in task.commands:
            print(f"\n Running: {cmd}")
            result = subprocess.run(cmd, shell=True, cwd=self.repo_path)
            if result.returncode != 0:
                print(f"[FAIL] Command failed with exit code {result.returncode}")
                task.status = TaskStatus.FAILED
                self.save_tasks()
                return False
        
        # Run validation
        print(f"\n Validating task completion...")
        for validation_cmd in task.validation:
            print(f"  Checking: {validation_cmd}")
            result = subprocess.run(validation_cmd, shell=True, cwd=self.repo_path, 
                                    capture_output=True, text=True)
            if result.returncode != 0:
                print(f"  [FAIL] Validation failed")
                print(result.stderr)
                task.status = TaskStatus.FAILED
                self.save_tasks()
                return False
            print(f"  [OK] Passed")
        
        task.status = TaskStatus.COMPLETE
        self.save_tasks()
        print(f"\n[OK] Task {task.id} completed successfully!")
        return True
    
    def execute_agent_task(self, task: Task) -> bool:
        """Execute a task via an agent"""
        print(f"[AGENT] Delegating to agent: {task.owner}\n")
        
        # Build agent prompt from task
        prompt = f"""Execute the following task:

Task ID: {task.id}
Name: {task.name}
Phase: {task.phase}
Estimated Time: {task.estimated_hours} hours

Success Criteria:
{chr(10).join('- ' + c for c in task.success_criteria)}

Validation Commands:
{chr(10).join('$ ' + v for v in task.validation)}

Repository Path: {self.repo_path}

Please execute this task and report completion status.
"""
        
        # For now, print agent invocation (would integrate with actual agent system)
        print(f"Agent Prompt:\n{prompt}")
        print(f"\n[WARNING]  Agent integration not yet implemented.")
        print(f"Please execute this task manually and mark as complete.\n")
        
        response = input("Mark task as complete? [y/N]: ").lower()
        if response == 'y':
            task.status = TaskStatus.COMPLETE
            self.save_tasks()
            return True
        else:
            task.status = TaskStatus.PENDING
            self.save_tasks()
            return False
    
    def show_status(self):
        """Display current status of all tasks"""
        print(f"\n{'='*70}")
        print(f"IMPLEMENTATION ROADMAP - STATUS DASHBOARD")
        print(f"{'='*70}\n")
        
        for phase in [1, 2, 3]:
            phase_tasks = [t for t in self.tasks.values() if t.phase == phase]
            if not phase_tasks:
                continue
            
            complete = sum(1 for t in phase_tasks if t.status == TaskStatus.COMPLETE)
            total = len(phase_tasks)
            pct = (complete / total * 100) if total > 0 else 0
            
            print(f"Phase {phase}: {complete}/{total} tasks complete ({pct:.0f}%)")
            
            for task in sorted(phase_tasks, key=lambda t: t.id):
                status_icon = {
                    TaskStatus.PENDING: "[PENDING] ",
                    TaskStatus.IN_PROGRESS: "[RUNNING] ",
                    TaskStatus.BLOCKED: "[BLOCKED]",
                    TaskStatus.COMPLETE: "[OK]",
                    TaskStatus.FAILED: "[FAIL]",
                }[task.status]
                
                print(f"  {status_icon} {task.id}: {task.name} ({task.owner})")
            print()
    
    def calculate_health_score(self) -> int:
        """Calculate current repository health score"""
        score = 36  # Baseline
        
        # Phase 1 completion: +24 points
        phase1_tasks = [t for t in self.tasks.values() if t.phase == 1]
        phase1_complete = sum(1 for t in phase1_tasks if t.status == TaskStatus.COMPLETE)
        phase1_total = len(phase1_tasks)
        if phase1_total > 0:
            score += int(24 * phase1_complete / phase1_total)
        
        # Phase 2 completion: +15 points
        phase2_tasks = [t for t in self.tasks.values() if t.phase == 2]
        phase2_complete = sum(1 for t in phase2_tasks if t.status == TaskStatus.COMPLETE)
        phase2_total = len(phase2_tasks) if len(phase2_tasks) > 0 else 1
        score += int(15 * phase2_complete / phase2_total)
        
        # Phase 3 completion: +10 points
        phase3_tasks = [t for t in self.tasks.values() if t.phase == 3]
        phase3_complete = sum(1 for t in phase3_tasks if t.status == TaskStatus.COMPLETE)
        phase3_total = len(phase3_tasks) if len(phase3_tasks) > 0 else 1
        score += int(10 * phase3_complete / phase3_total)
        
        return min(score, 85)  # Cap at target

def main():
    """Main orchestrator entry point"""
    repo_path = Path(__file__).parent.parent
    orchestrator = TaskOrchestrator(repo_path)
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "status":
            orchestrator.show_status()
            health = orchestrator.calculate_health_score()
            print(f"Current Health Score: {health}/100")
        
        elif command == "next":
            ready_tasks = orchestrator.get_ready_tasks()
            if ready_tasks:
                next_task = ready_tasks[0]
                print(f"Next task: {next_task.id} - {next_task.name}")
                orchestrator.execute_task(next_task.id)
            else:
                print("No tasks ready to execute (check dependencies)")
        
        elif command == "execute":
            if len(sys.argv) < 3:
                print("Usage: orchestrator.py execute <task_id>")
                sys.exit(1)
            task_id = sys.argv[2]
            if task_id in orchestrator.tasks:
                orchestrator.execute_task(task_id)
            else:
                print(f"Task {task_id} not found")
        
        elif command == "auto":
            print("[ACTION] Auto-execution mode: executing all ready tasks...\n")
            while True:
                ready_tasks = orchestrator.get_ready_tasks()
                if not ready_tasks:
                    print("[OK] No more tasks ready. Check status for blockers.")
                    break
                
                next_task = ready_tasks[0]
                success = orchestrator.execute_task(next_task.id)
                if not success:
                    print(f"[PENDING]  Paused at task {next_task.id}")
                    break
        
        else:
            print(f"Unknown command: {command}")
            print("Usage: orchestrator.py [status|next|execute <id>|auto]")
    
    else:
        orchestrator.show_status()
        health = orchestrator.calculate_health_score()
        print(f"Current Health Score: {health}/100\n")
        print("Commands:")
        print("  status         Show task status")
        print("  next           Execute next ready task")
        print("  execute <id>   Execute specific task")
        print("  auto           Auto-execute all ready tasks")

if __name__ == "__main__":
    main()
