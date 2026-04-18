Bangalore House Price Prediction
This project is my take on the classic Bangalore House Price dataset. The goal was to build a reliable model that can estimate house prices based on features like location, square footage, and the number of bedrooms/bathrooms.

Why I built this
I wanted to go beyond just running a model; I wanted to understand the data, handle the messy parts, and actually build something that makes sense in the real world.

How I tackled the data
The dataset was quite noisy, so I spent a good chunk of time cleaning it up:

Cleaning: Handled missing values and turned those tricky "range" values in total_sqft into averages.

Domain Logic: I applied some common sense filters—for instance, I removed records where the square footage per bedroom was too low (less than 300 sqft), as those just didn't look like actual houses.

Outliers: I used standard deviation to filter out weird price points for each location, which really helped clean up the target variable.

Feature Engineering: Grouped rare locations into an "other" category to keep the model from getting overwhelmed by too many unique labels.

What worked best
I experimented with a few different approaches to see what would give the most consistent results:

Linear Regression: My baseline, which got me to about 76% accuracy.

Ridge & Lasso: After scaling the data and tuning the hyperparameters, these both gave me a solid 80% accuracy, which I felt was a great spot to land on.

Decision Trees: They didn't perform as well here (~71%), likely because the pricing structure is fairly linear.

How to use it
If you want to run this yourself:

You'll need the bangalore_house_price_model.pkl file.

Use the columns.json file to ensure the input data matches the format the model was trained on.

Just load the model using joblib and pass in your inputs!

Lessons learned
The biggest takeaway for me wasn't the algorithms—it was the data prep. Spending the time to understand the "why" behind the outliers and grouping the locations made a much bigger difference than just picking a complex model.

Feel free to poke around the notebook if you're curious about the specific steps. If you have any feedback or want to suggest an improvement, I'm all ears!