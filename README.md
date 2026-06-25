
# Control-dataset
*Assignment for Fundamental Research in Machine and Deep Learning course at TU Delft*


**Disclaimer: The full dataset was too big to upload but you can create it exactly by running the code in the [Github](https://github.com/sandemiroren1/control-dataset). A sample of 1000 datapoints has also been provided in the repository**



While designing a dataset I wanted to ensure that the property it is testing was interesting, but not extremely niche. Hence, I decided that I wanted to design a dataset based on a simple rule, but a rule which has interesting implications. I wanted to test how the models would change their classification, when there was perhaps another object of interest, hiding subtly in the image...

## Pre-requisites
Before moving on further, I want to give substance to some of the terminology I will be using. This methodology is based on overlaying/mixing two images together with varying degrees of opacity. Namely, for a pair of images $(i_1,i_2)$ I define $\alpha\in[0,0.5]$ to be the opacity of the first image $i_1$. This value has a maximum of 0.5 as any value that is higher is the same task but with the images swapped. Lastly, the resulting image is obtained by summing up the pixel values as the following in *Equation 1*.


*Equation 1*



$$i'=\alpha\cdot i_1 + (1-\alpha)\cdot i_2$$


I say that an object's label is the "main label" of a mixture of images if its the object with the highest opacity value. I also refer to that object as the "dominant object" in the picture. To gain more intuition on the results of the mixture process you can refer to *Figure 1* which shows results for differing $\alpha$ values.


**Figure 1**: The blending of two images with $\alpha\in\{0,0.1,0.2,\ldots,1\}$. Up until the 6th image, the main object is the yellow parachute as it has a higher opacity.
![Example image](example.png)

## The purpose of the dataset
The main purpose of this dataset is to test if an image recognition model can correctly recognize the "main label" of an image when there are two images overlapped with one another. Consequently, this also tests if the model can recognize an object when there is another motif in the picture that might belong to another class, which models fall victim to [1]. However, while [1] did show that models can get "distracted" by another object in the picture, they did so by applying a "patch"/"sticker" to the image that resembles another object. Although that is an interesting result, I think it is also interesting to have a dataset that checks how models behave when that object's image is added faintly to an image. 


Furthermore, these examples are usually created adversarially and are mostly arbitrary, with their applications and implications being unclear [2]. So I believe my dataset can offer an interesting perspective in this area of research as it can provide "hard" images that test for a model's robustness against background motifs that might distract it, a scenario that can have more applications.[3] showed state-of-the-art models can be blind to objects by the placement of another object nearby, for which they show an example of an elephant being added next a TV remote and the model suddenly being blind to both. Hence, my dataset can provide another perspective to this phenomenon. Conversely, the dataset can also be used to test the models ability to detect subtle details when there is an overpowering object on the way[3]. 

## Motivation for the dataset doing its job


By overlaying two images on top of each other at differing opacity rates, the dataset tests the extent that the model can get distracted from the more dominant object. The dataset features images created with low $\alpha$ values in which the features of the non-dominant object are more subtle. This tests if the model gets "distracted" easily from the dominant object in the picture if a small motif of another object is present. Which, as mentioned already seemed to provide results in [1]. Moreover, the dataset also provides harder examples with the use of $\alpha=0.3,0.5$ which should also test the models behaviour when the non-dominant object's features are more prominent. All of these can give valueable insight to a model's tendancy to get distracted or to recognize the object thats more prominent, which can have interesting applications in robustness research.
### What is inside the box
Here I detail how I created the dataset and then give examples from it. The full code and the dataset can be found in: https://github.com/sandemiroren1/control-dataset. To recreate the dataset you must run the code but a sample of a 1000 images has been provided.

### Creation
The dataset was created using images from  [ImageNette](https://github.com/fastai/imagenette). Given an $\alpha$ my code picks out two random images from ImageNette and then blends them, using *Equation 1*. The resulting data point is 5-tuple that consists of: 
* The newly created image itself
* Label of Image 1 
* Label of Image 2 
* The main label of the new image
* The $\alpha$ value.
The dataset contains a total of 120,000 images. This was accomplished by creating 40,000 images per $\alpha$ value in the set $\{0,1,0.3,0.5\}$.


The dataset was created while ensuring that there aren't any duplicate images in the dataset. 
### Examples 
**Figure 2**: A garbage truck and a gas pump mixed together with $\alpha=0.1$ and the garbage truck being the dominant object.


![Example 2](examples/example1.png) 

In Figure 2 we can see a subtle mixture of two images. To the human eye, the garbage truck is prominent but the gas pump is not. With the use of this dataset, it can be observed if a model fails at even the slightest of resemblense to another object. 


**Figure 3**: (a) A picture of a dog mixed with a church with the dog being dominant, $\alpha=0.3$. (b) A picture of a dog and a parachute with $\alpha=0.5$. Both objects are equally dominant.


![Example 2](examples/example2.png) ![Example 3](examples/example3.png)


The dataset also provides harder examples as it can be seen in *Figure 3*. In both examples it is a bit harder to tell which object is the prominent one, in fact for *Figure 3.b* one there isn't one! I believe that training a model to be correct on these examples can provide an interesting aspect of robustness. Moreover, it can also be interesting to see *how* the model changes its classification. Does it perhaps grok that the main object is a dog, but suddenly labels it as a Golden Retreiver rather than a Husky when the non-dominant picture is changed?


### Conclusion

In conclusion, in this post I provide a dataset that can be used to test a model's ability to correctly distinguish the main object in an image when there is a picture of another object subtly overlayed on the image. This dataset was created by using images from a well-known source and then combining pairs from them into one image. This provides a different glance at the robustness of an image classification model in a scenario in which there are subtle features of an object other than the object that should be recognized. My dataset fills a unique gap in the existing literature and dataset has 120,000 images that have varying degrees of subtlety in how they overlay the features of the other image. I also provide the code for the dataset so that any similar dataset can be created.






## Citations 
[1] https://arxiv.org/abs/1712.09665
[2] https://arxiv.org/pdf/1807.06732
[3] https://arxiv.org/pdf/1808.03305

