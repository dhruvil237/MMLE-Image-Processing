# Modified code of MMLE

## Changes made
### Change 1: 
The formula for Lcolor is improved by including a weighting factor for each channel, as the current formula treats all channels equally. This modification allows the model to adapt to images with different color distributions, rather than using a fixed set of parameters for all images. 

Weighted formula:
Lcolor = w_l*(I¯l - I¯m) + w_s*(I¯l - I¯s)

In this modified formula, w_l and w_s are weighting factors for the largest and smallest channels, respectively. These weights could be determined based on the characteristics of the image being processed, or could be set to fixed values if appropriate.



### Change 2:
The formula used in the MMLE model to balance the color between the a and b channels of the CIELAB space. The current formula is: image
Ibc(a,b) = Ib(a,b) + (I¯a - I¯b) * (I¯a + I¯b) / 2
Iac(a,b) = Ia(a,b) + (I¯b - I¯a) * (I¯b + I¯a) / 2

where I¯a and I¯b are the mean values of the a and b channels, respectively. This formula is based on the assumption that the mean values of the a and b channels are the same for the original and processed images. However, this assumption is not always true, and can lead to color distortion in the processed image. For example, if the mean value of the a channel is higher in the original image, then the formula will increase the value of the a channel in the processed image, which will result in a reddish tint. This can be seen in the following example, where the original image has a reddish tint, and the processed image has a greenish tint:



Adaptive balancing based on the color histogram:
Rather than using the mean values of the a and b channels to perform color balancing, the formula could be modified to use information from the color histogram of the image. For example, a histogram-based approach could be used to determine the regions of the color space where the distribution of colors is skewed, and then apply different balancing factors in these regions. This would allow the formula to adapt to images with different color distributions, rather than using a fixed set of parameters for all images.

Let H(a, b) be the color histogram of the image in the CIELAB space, where a and b are the coordinates of a point in the color space. To adaptively balance the color channels, we can modify the original formula as follows:
Ibc(a,b) = Ib(a,b) + f(a,b) * (I¯a - I¯b) * (I¯a + I¯b) / 2
Iac(a,b) = Ia(a,b) + (1 - f(a,b)) * (I¯b - I¯a) * (I¯b + I¯a) / 2

where f(a,b) is a function that depends on the color distribution at each point in the histogram, and determines the relative weights to be used for the a and b channels. This function could be defined in a variety of ways, depending on the desired behavior. For example, one possible function would be:

f(a,b) = 0.5 + k * (H(a,b) - H_mean) / H_std

where H_mean and H_std are the mean and standard deviation of the histogram, respectively, and k is a scaling factor. This function would give greater weight to the channel with the higher color frequency at each point, while also allowing for some adaptation based on the overall distribution of colors in the image.


Making the above two changes increases: Colorfulness Contrast Fog Density Index CCF, CCF which considers the colorfulness, contrast, and fog density indices to assess an underwater image.



## Testing
```
1. Clone repo
2. install all the dependencies
2. python -m main.py
```


