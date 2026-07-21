# Into to Jenkins and CI/CD

![alt text](<Diagram/Jenkins CICD Pipeline.png>)

* What is CI
  * CI stands for Continuous Integration
  * Often triggered by: A developer push their code changes to a shared repository
  * Tests are automatically run on the code before the tested code is integrated/merged into the main code base 

* What is CD?
  * CD can mean either:
    * Continuous Deployment
      * Making sure that the software is always in a deployable state
      * We need code that can be pushed to production at any time (that may take the form of an artifact)
    * Continuous Delivery
      * Does what continuous delivery does, but goes one step further, it also deploys the code

* What is Jenkins?  
Jenkins is an open-source automation server used to automate building, testing, and deployment of code. It allows developers to automatically integrate code changes, run automated tests and release software quickly and reliably.

* Why use Jenkins?
  * Benefits:
    * Automation (less human error and manual intervention)
    * Extensible via the plugins (has a lot of support for other tools/languages/programs)
    * Scalability
    * Community Support
    * Cross-platform
  * Disadvantages:
    * Complex for beginners
    * Maintenance overhead
    * Can be resource-intensive
    * User interface 

* Stages of Jenkins
  1. Source Code Management (SCM) (part of CI)
  2. Build (part of CI)
  3. Test (part of CI)
  4. Integrate/merge code in main code base (part of CI)
  5. Package (part of CD)
  6. Deploy (If pipeline is doing Continuous Deployment)
  7. Monitor (If pipeline is doing Continuous Deployment)

* What alternatives are there for Jenkins
  * GitHub Actions
  * GitLab
  * Azure DevOps
  * CircleCI
  * TravisCI
  * Bamboo
  * TeamCity
  * GoCD

* Why build a pipeline? 
  * Faster to get the latest version of the product into the hands of end users (Faster time to market)
  * Faster feedback cycle
  * Improved quality
  * Reduced risk
  * Improved efficiency and productivity