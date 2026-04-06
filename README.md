# AI Code Review Environment

Simulates GitHub PR review for AI agents.

## Tasks
- Easy: Syntax bug detection  
- Medium: Logical/security bug detection  
- Hard: Full PR evaluation  

## Actions
- comment  
- approve  
- request_changes  

## Run
python inference.py

## Advanced Evaluation Design

This environment evaluates:
- Issue detection accuracy
- Explanation quality
- Severity-aware scoring

### Reward Design
- Partial rewards for correct issue identification
- Additional rewards for meaningful explanations
- Penalties for irrelevant comments

### Issue Types
- Security vulnerabilities (high severity)
- Performance inefficiencies (medium severity)
- Syntax errors (high severity)
