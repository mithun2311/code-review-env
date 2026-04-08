from .models import Observation, Action
from .tasks import TASKS
from .graders import grade

class CodeReviewEnv:

    def __init__(self, task_name="easy_bug_detection"):
        self.task_name = task_name
        self.task = TASKS[task_name]
        self.reset()

    def reset(self):
        self.comments = []
        self.step_count = 0
        return Observation(
            pr_id=1,
            files_changed=self.task["files"],
            comments_so_far=[],
            step_count=0
        )

    def step(self, action: Action):
        self.step_count += 1
        reward = 0.0
        done = False
        error = None

        expected_types = [i["type"] for i in self.task["expected_issues"]]

        if action.action_type == "comment":
            comment = action.comment or ""
            self.comments.append(comment)

            # smarter reward
            if any(issue in comment.lower() for issue in expected_types):
                reward = 0.3
            else:
                reward = 0.05

        elif action.action_type in ["approve", "request_changes"]:
            score = grade(self.comments, self.task["expected_issues"])
            MIN_VALID_SCORE = 0.01
            MAX_VALID_SCORE = 0.99
            reward = min(max(score, MIN_VALID_SCORE), MAX_VALID_SCORE)
            done = True

        obs = Observation(
            pr_id=1,
            files_changed=self.task["files"],
            comments_so_far=self.comments,
            step_count=self.step_count
        )

        return obs, reward, done, {"error": error}

    def state(self):
        return {
            "comments": self.comments,
            "steps": self.step_count
        }
