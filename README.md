# Control-dataset
*Assignment for Fundamental Research in Machine and Deep Learning course at TU Delft*

While designing a dataset I wanted to ensure that the property it is testing was interesting, but not extremely niche. Hence, I decided that I wanted to design a dataset based on a simple rule, but a rule which has interesting implications. I wanted to test how the models would change their classification, when there was perhaps another object of interest, hiding subtly in the image...

### Pre-requisites
Before moving on further, I want to give substance to some of the terminology I will be using. This methodology is based on overlaying two images together with varying degrees of opacity. Namely, for a pair of images $(i_1,i_2)$ we define $\alpha\in[0,1]$ to be the opacity of the first image $i_1$. Then the resulting image is obtained by summing up the pixel values as $i'=\alpha\cdot i_1 + (1-\alpha)\cdot i_2$.
This led me to make a test set that tests the ability of a image recognition model in not getting distracted from the "main image 
