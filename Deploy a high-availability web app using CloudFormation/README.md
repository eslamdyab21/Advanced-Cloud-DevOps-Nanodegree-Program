# Project Introduction

As your final project, you'll be faced with a real scenario.

Creating this project will give you the hands-on experience you need 
to confidently talk about infrastructure as code. We have chosen a 
realistic scenario where you will deploy a dummy application (a sample 
JavaScript or HTML file) to the Apache Web Server running on an EC2 
instance.

There will be two parts to this project:

- **Diagram**: You'll first develop a diagram that you
can present as part of your portfolio and as a visual aid to understand
the CloudFormation script.
- **Script (Template and Parameters)**: The second part is to interpret the instructions and create a matching CloudFormation script.

# 

## Scenario

Your company is creating an Instagram clone called Udagram.

Developers want to deploy a new application to the AWS infrastructure.

You have been tasked with provisioning the required infrastructure and deploying a **dummy application**, along with the necessary supporting software.

This needs to be automated so that the infrastructure can be 
discarded as soon as the testing team finishes their tests and gathers 
their results.

## Server specs

1. create a **Launch Configuration** for
the application servers in order to deploy **four servers**, two located in each of your private subnets(**2 private subnets**). The launch configuration will be used by
an **auto-scaling group**.
———> **four servers, two in each private subnets**
2. two vCPUs and at least 4GB of RAM. The Operating System
to be used is Ubuntu 18. So
3. allocate at least 10GB of disk space.

## Security Groups and Roles

- create an **IAM Role** that allows your instances to use the S3 Service.
- Udagram communicates on the default `HTTP Port: 80`, so the servers will need this inbound port open and using it with the **Load Balancer** and the **Load Balancer Health Check**. As for outbound, the servers will need unrestricted internet access to be able to download and update their software.
———> need NAT between the servers and the Gateway
- **The load balancer allows all public traffic** `(0.0.0.0/0)` on `port 80` **inbound**, which is the default `HTTP port`. Outbound, it will only be using `port 80` to reach the internal servers.
- **The application is deployed into private subnets** with a **Load Balancer located in a public subnet**.
- One of the output exports of the **CloudFormation** script is the public URL of the **LoadBalancer**.
<br/>

- we can destroy the entire infrastructure and build it back up without any manual steps required, other than running the **CloudFormation** script.
- used a bastion host (jump box)
to allow you to SSH into your private subnet servers. This bastion host
would be on a Public Subnet with `port 22` open only to your home `IP address`, and it would need to have the private key that you use to access the other servers.
<br/>
<br/>
## Some screenshots of the outputs

---

## The Developed Diagram

![Flowcharts.png](Deploy%20a%20high-availability%20web%20app%20using%20CloudForm%2078bbf1993ed346e5a9222cee72afbc95/Flowcharts.png)
<br/>
## The jump box

![Screenshot from 2022-08-05 04-53-35.png](Deploy%20a%20high-availability%20web%20app%20using%20CloudForm%2078bbf1993ed346e5a9222cee72afbc95/Screenshot_from_2022-08-05_04-53-35.png)
<br/>
## Some outputs of the two created stacks

![Untitled](Deploy%20a%20high-availability%20web%20app%20using%20CloudForm%2078bbf1993ed346e5a9222cee72afbc95/Untitled.png)
<br/>

## The load balance running on this URL:
Udagr-WebAp-1DUGL1NG0WO25-763462357.us-east-1.elb.amazonaws.com

![Untitled](Deploy%20a%20high-availability%20web%20app%20using%20CloudForm%2078bbf1993ed346e5a9222cee72afbc95/Untitled%201.png)