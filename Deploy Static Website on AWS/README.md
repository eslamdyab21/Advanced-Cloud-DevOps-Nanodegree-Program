Deploy Static Website on AWS Project Overview
================

The cloud is perfect for hosting static websites that only include HTML, CSS, and JavaScript files that require no server-side processing. The whole project has two major intentions to implement:

*   Hosting a static website on S3

*   Accessing the cached website pages using CloudFront content delivery network (CDN) service. Recall that CloudFront offers low latency and high transfer speeds during website rendering.
<br>
<br>

### In this project, we will deploy a static website to AWS by performing the following steps:

1.  create a public S3 bucket and upload the website files to your bucket.

2.  configure the bucket for website hosting and secure it using IAM policies.

3.  speed up content delivery using AWS’s content distribution network service, CloudFront.

4.  access your website in a browser using the unique CloudFront endpoint.


<br><br>
1
-

* * *

<br>
*   Here is the created bucket with name `my-2031830-bucket-for-website-project`



[![](Deploy%20Static%20Website%20on%20AWS%206d50023531c2454d89058da199e46f0f/Untitled.png)](Deploy%20Static%20Website%20on%20AWS%206d50023531c2454d89058da199e46f0f/Untitled.png)

<br><br>

*   and here is the website related files required to host it, they are html,css and java files.

[![](Deploy%20Static%20Website%20on%20AWS%206d50023531c2454d89058da199e46f0f/Untitled%201.png)](Deploy%20Static%20Website%20on%20AWS%206d50023531c2454d89058da199e46f0f/Untitled%201.png)
<br><br><br>
2
-

* * *
<br>
*   Here we configured the website bucket to `enable the static website hosting` and the index file is passed to the index document.







[![](Deploy%20Static%20Website%20on%20AWS%206d50023531c2454d89058da199e46f0f/Untitled%202.png)](Deploy%20Static%20Website%20on%20AWS%206d50023531c2454d89058da199e46f0f/Untitled%202.png)


<br><br>
*   In order for the user to see the website it needs to publicly available, this is done by making an `IAM policy` for the website bucket which allows getting website bucket files to anyone. Making it publicly available.

[![](Deploy%20Static%20Website%20on%20AWS%206d50023531c2454d89058da199e46f0f/Untitled%203.png)](Deploy%20Static%20Website%20on%20AWS%206d50023531c2454d89058da199e46f0f/Untitled%203.png)

<br><br>
*   Now we can visit the hosted website through the link shown in bucket properties in the static hosting option (`Bucket website endpoint`)



[![](Deploy%20Static%20Website%20on%20AWS%206d50023531c2454d89058da199e46f0f/Untitled%204.png)](Deploy%20Static%20Website%20on%20AWS%206d50023531c2454d89058da199e46f0f/Untitled%204.png)

*   But our requests is going straight to the bucket every-time we visit the website without any cashing. This can take some time especially if the bucket location was far from the user. That’s why we will use the CloudFront next to speed up the content delivery.

<br><br>

3
-

* * *
<br>
*   Here we create the CloudFront distribution and link it to the website bucket using the domain name provided above in the website bucket static hosting option.



[![](Deploy%20Static%20Website%20on%20AWS%206d50023531c2454d89058da199e46f0f/Untitled%205.png)](Deploy%20Static%20Website%20on%20AWS%206d50023531c2454d89058da199e46f0f/Untitled%205.png)

<br> <br>
*   Here is the CloudFront distribution enabled and you can see it’s domain name for our website.
<br> <br>

[![](Deploy%20Static%20Website%20on%20AWS%206d50023531c2454d89058da199e46f0f/Untitled%206.png)](Deploy%20Static%20Website%20on%20AWS%206d50023531c2454d89058da199e46f0f/Untitled%206.png)

[![](Deploy%20Static%20Website%20on%20AWS%206d50023531c2454d89058da199e46f0f/Untitled%207.png)](Deploy%20Static%20Website%20on%20AWS%206d50023531c2454d89058da199e46f0f/Untitled%207.png)
