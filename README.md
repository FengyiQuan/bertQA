## Bert-QA
With the increasing demand for artificial intelligence applications in various industries, deploying machine learning models has become a crucial task for data scientists and developers. One of the most popular and powerful machine learning models for natural language processing is the Bert-QA (Question Answering) model. However, deploying Bert-QA models can be a complex and time-consuming process.

Fortunately, with the help of cloud services such as AWS App Runner and ECR, deploying Bert-QA models has become easier and more accessible. AWS App Runner is a fully managed service that allows you to quickly deploy containerized applications, while ECR is a fully-managed Docker container registry that makes it easy to store, manage, and deploy container images.

### ECR (Elastic Container Registry)
ECR stands for Elastic Container Registry. It is a fully-managed Docker container registry provided by Amazon Web Services (AWS) that makes it easy to store, manage, and deploy container images. ECR allows you to securely store and manage your Docker images in a highly available and scalable environment, and easily integrate with other AWS services such as Amazon ECS, Amazon EKS, and AWS App Runner.

By using ECR, you can easily manage your container images at scale, and deploy them quickly and reliably to your container-based applications running on AWS. ECR also provides secure access controls, image scanning for vulnerabilities, and encryption of your container images at rest and in transit.

### AppRunner
AWS App Runner is a fully managed service provided by Amazon Web Services (AWS) that allows you to quickly deploy containerized applications. With App Runner, you can easily build, deploy, and run containerized applications without needing to manage infrastructure, containers, or orchestration. App Runner is designed to simplify the process of deploying containerized applications and make it accessible to developers without requiring deep knowledge of AWS or containerization.

Using App Runner, you can deploy containerized applications from a variety of sources, including public and private container registries, source code repositories, and container images stored in Amazon Elastic Container Registry (ECR). App Runner also supports automatic scaling and provides metrics and logs to help you monitor your application's performance.

App Runner can be used to deploy a wide range of applications, including web applications, APIs, microservices, and machine learning models. It is suitable for both small and large-scale deployments, and offers a simple pricing model based on usage and resources consumed.

### Example
```json
{
    "context": "The Intergovernmental Panel on Climate Change (IPCC) is a scientific intergovernmental body under the auspices of the United Nations, set up at the request of member governments. It was first established in 1988 by two United Nations organizations, the World Meteorological Organization (WMO) and the United Nations Environment Programme (UNEP), and later endorsed by the United Nations General Assembly through Resolution 43/53. Membership of the IPCC is open to all members of the WMO and UNEP. The IPCC produces reports that support the United Nations Framework Convention on Climate Change (UNFCCC), which is the main international treaty on climate change. The ultimate objective of the UNFCCC is to \"stabilize greenhouse gas concentrations in the atmosphere at a level that would prevent dangerous anthropogenic [i.e., human-induced] interference with the climate system\". IPCC reports cover \"the scientific, technical and socio-economic information relevant to understanding the scientific basis of risk of human-induced climate change, its potential impacts and options for adaptation and mitigation.\"", 
    "question": "What organization is the IPCC a part of?"
}
```
```
{
    "score": 0.48815739154815674,
    "start": 118,
    "end": 132,
    "answer": "United Nations"
}
```
```json
{
    "context" : "New York (CNN) -- More than 80 Michael Jackson collectibles -- including the late pop star's famous rhinestone-studded glove from a 1983 performance -- were auctioned off Saturday, reaping a total $2 million. Profits from the auction at the Hard Rock Cafe in New York's Times Square crushed pre-sale expectations of only $120,000 in sales. The highly prized memorabilia, which included items spanning the many stages of Jackson's career, came from more than 30 fans, associates and family members, who contacted Julien's Auctions to sell their gifts and mementos of the singer. Jackson's flashy glove was the big-ticket item of the night, fetching $420,000 from a buyer in Hong Kong, China. Jackson wore the glove at a 1983 performance during \"Motown 25,\" an NBC special where he debuted his revolutionary moonwalk. Fellow Motown star Walter \"Clyde\" Orange of the Commodores, who also performed in the special 26 years ago, said he asked for Jackson's autograph at the time, but Jackson gave him the glove instead. \"The legacy that [Jackson] left behind is bigger than life for me,\" Orange said. \"I hope that through that glove people can see what he was trying to say in his music and what he said in his music.\" Orange said he plans to give a portion of the proceeds to charity. Hoffman Ma, who bought the glove on behalf of Ponte 16 Resort in Macau, paid a 25 percent buyer's premium, which was tacked onto all final sales over $50,000. Winners of items less than $50,000 paid a 20 percent premium.\"",
    "question" : "Where was the Auction held?"
}
```
```json
{
    "score": 0.2847529351711273,
    "start": 259,
    "end": 282,
    "answer": "New York's Times Square"
}
```

### Deploy the Docker image in AWS App Runner

Log in to the AWS Console and navigate to the AWS App Runner service.

Click on "Create an App Runner service" and select "Container image" as the source.

Select "ECR" as the image provider and choose the ECR repository and image tag that you pushed earlier.

Configure the runtime settings for your Bert-QA model, including the command to run your application and any environment variables that it requires.

Choose the VPC and subnet where you want to run your Bert-QA model and configure any security settings that are necessary.

Click on "Create service" to deploy your Bert-QA model in App Runner.

Once the deployment is complete, you can access your Bert-QA model by using the App Runner service URL.