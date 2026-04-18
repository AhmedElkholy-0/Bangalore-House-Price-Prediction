Bangalore House Price Prediction
This project is my take on the Bangalore House dataset. My goal was to build a reliable model that estimates property prices by accounting for features like location, square footage, and property configuration.

Why I built this
I wanted to go beyond just running a model. I wanted to understand the data, handle the "messy" parts, and build a pipeline that makes sense in a real-world context.

The Data Pipeline
The dataset was quite noisy, so I focused on a structured data-preprocessing pipeline:

Data Cleaning: Handled missing values and standardized total_sqft by converting ranges into numerical averages.

Domain Logic: I applied common-sense filtering. For instance, I removed records where the square footage per bedroom was unrealistically low (e.g., < 300 sqft), which helped eliminate data entry errors.

Outlier Handling: I used Standard Deviation filtering per location to identify and remove price anomalies, which significantly improved the model's target variable consistency.

Feature Engineering: Grouped rare locations into an "other" category to prevent high-cardinality issues and ensure the model remains robust.

Model Selection & Performance
I experimented with different approaches to find the right balance between complexity and performance:

Linear Regression: My baseline approach (~76% accuracy).

Ridge & Lasso: After scaling the data and tuning hyperparameters, these gave me a solid 80% accuracy, which I found to be the sweet spot for this dataset.

How to use it
Everything is included in this repository. To get started:

Clone the repo.

Install dependencies: pip install -r requirements.txt

Run the predictor: python predict.py

Lessons Learned
The biggest takeaway for me wasn't the algorithms—it was the data prep. Investing time in understanding the "why" behind the outliers and grouping locations made a much bigger difference in performance than simply choosing a more complex model.

I'm always looking to refine my skills, so I'd appreciate any insights you might have. Feel free to explore the notebook.ipynb for the full breakdown!