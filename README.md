
# Microsoft Entra ID Lifecycle Workflows: End-to-End Identity Automation Project
### Project Overview

This project demonstrates the design, implementation, and governance of automated identity lifecycle management using Lifecycle Workflows in Microsoft Entra ID. The objective is to automate Joiner-Mover-Leaver (JML) processes, reduce manual administration, improve security posture, and ensure compliance. The project progresses from beginner to senior-level implementations, showcasing identity governance maturity in enterprise environments

# Phase 1: demonstrating Lifecycle Workflows
### Objective
### Implement the fundamentals of Lifecycle Workflows and automate simple user onboarding tasks.

Tasks Implemented
```
1. Enable Lifecycle Workflows.
2. Create test users.
3. Configure user attributes:
4. Department
5. Manager
6. Employee Hire Date
7. Create a basic Joiner workflow.
8. Trigger workflow manually.
```

Workflow Actions
- Send a welcome email.
* Generate Temporary Access Pass (TAP).
+ Notify manager.

Documentation Evidence

* Screenshots of workflow creation.
- Workflow execution history.
+ Audit logs.

Skills Demonstrated

+ Identity Governance basics
- Attribute management
* Workflow monitoring



# Phase 2: Implementing Joiner Automation

## Objective

Automate onboarding for new employees based on hire date.

## Implementation

Create a Joiner Workflow that starts automatically when

```
employeeHireDate = Today
```

Automated Actions
```
1. Generate Temporary Access Pass.
2. Send onboarding email.
3. Notify HR.
4. Notify hiring manager.
```

## Expected Outcome

New employees receive secure access on their first day without administrator intervention.

1. Security Benefits
2. Reduces manual provisioning errors.
3. Accelerates user productivity.
4. Enforces Zero Trust onboarding.


# Phase 3: Mover Workflow Implementation
## Objective

Automate access reviews and notifications when employees change roles.

```
Scenario
```

A user moves from.

```
Department: Sales → Finance
```

## Workflow Actions
1. Notify the old manager.
2. Notify new manager.
3. Trigger access review.
4. Document identity changes



# Phase 4: Advanced Level – Leaver Workflow
## Objective

Automate offboarding processes to minimize insider risk.

 Workflow Trigger. The user account is disabled, or the employee leaves the organization.

## Automated Actions
```
1. Notify manager.
2. Notify the security team.
3. Remove group memberships.
4. Revoke sessions.
5. Disable account.
6. Archive mailbox.
```

## Security Benefits
```
Automated offboarding significantly reduces the risk of orphaned accounts and unauthorized access.
```

# Phase 5: Group-Based Governance
## Objective

Automate privileged access governance.

## Implementation to create workflows for:

1. Privileged role assignments
2. Administrative users
3. Contractors

 ```
Example
```
When a contractor reaches the expiration date:
```
employeeLeaveDate = Today
```

## Actions:
```
1. Disable account.
2. Remove licenses.
3. Notify sponsor.
```
## Governance Outcome
```
Improved compliance with least privilege and Just-In-Time access models.
```

# Phase 6:  Enterprise Join-Move-Leave(JML) Automation
## Objective

Design a full enterprise-grade Joiner-Mover-Leaver architecture.

+ Architecture Components
- Lifecycle Workflows
* Dynamic Groups
* Conditional Access
+ Privileged Identity Management (PIM)
- Access Reviews
* Entitlement Management

## Workflow Integration
```
New Employee
      ↓
Lifecycle Workflow
      ↓
Temporary Access Pass
      ↓
Dynamic Group Assignment
      ↓
Conditional Access Enforcement
      ↓
Access Reviews
      ↓
PIM Activation
```
## Enterprise Use Cases

1. New employee onboarding
2. Department transfers
3. Contractor expiration
4. Privileged user governance
5. Regulatory compliance
   
##Metrics Collected
1. Provisioning time reduction
2. Manual tasks eliminated
3. Audit events generated
4. Security incidents prevented

   
```  
Challenges Encountered
```

# During implementation, several challenges may arise:
```
Missing employee attributes.
Workflow execution delays.
Licensing requirements.
Incorrect manager assignments.
Dynamic group membership delays.
```
Troubleshooting these issues provides valuable hands-on experience in enterprise identity governance.

# Security and Compliance Considerations

## Lifecycle Workflows strengthen security by:
```
Enforcing Zero Trust principles.
Automating least privilege access.
Supporting compliance frameworks.
Maintaining audit trails.
Reducing human error.
```

# GitHub Repository Structure

Lifecycle-Workflows-Project/
```
│
├── README.md
├── Phase1-Beginner/
│   ├── Screenshots/
│   ├── Workflow-Configuration.md
│
├── Phase2-Joiners/
│   ├── Joiner-Workflow.md
│
├── Phase3-Movers/
│   ├── Mover-Workflow.md
│
├── Phase4-Leavers/
│   ├── Leaver-Workflow.md
│
├── Phase5-Governance/
│   ├── Contractors.md
│   ├── Privileged-Users.md
│
├── Phase6-Enterprise/
│   ├── Architecture-Diagram.png
│   ├── Lessons-Learned.md
│
└── LICENSE
```


# Conclusion
This project demonstrates progressive expertise in Microsoft Entra ID Lifecycle Workflows, moving from basic onboarding automation to enterprise identity governance. By documenting each phase with screenshots, workflow configurations, audit logs, and lessons learned, the project showcases practical Identity Security engineering skills applicable to modern Zero Trust environments.
