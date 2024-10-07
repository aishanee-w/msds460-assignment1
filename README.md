# msds460-assignment1
assignment 1: the diet problem

ASSIGNMENT INSTRUCTIONS:
Introduced by Stigler (1945) and discussed by Dantzig (1990), the diet problem is a classic problem in constrained optimization often used to introduce linear programming concepts. The diet problem has been studied extensively through the years (van Dooren 2018).

For this assignment, you need to construct a personalized diet using current recommended dietary allowances from the U.S. Food and Drug Administration, updated to account for recent research on sodium intake and health (Mente, O'Donnell, and Yusuf 2021). Interested in learning more about nutrition and healthy living? Check out Nutrients, an open-access journal, at its home page https://www.mdpi.com/journal/nutrients Links to an external site. .

The constraints for this linear programming problem, should consider seven components of nutrition and their daily values, as shown in the following table:

Sodium Maximum 5,000 milligrams (mg)

Energy Minimum 2,000 Calories (kilocalories, kcal)

Protein Minimum 50 grams (g)

Vitamin D Minimum 20 micrograms (mcg)

Calcium Minimum 1,300 milligrams (mg)

Iron Minimum 18 milligrams (mg)

Potassium Minimum 4,700 milligrams (mg)

Set this up as a standard linear programming problem with decision variables taking any non-negative values. In other words, partial servings are permitted.  

For nutritional constraints, consider setting these to satisfy a weekly diet. That is, multiply each daily requirement by seven (7).

Nutrition labels on packaged foods should contain information about these eight components of nutrition along with other components. Each of the components represents a constraint in the linear programming problem you are developing.

To adapt the problem to your personal diet, collect nutrition facts from five packaged food items in your household. Use packaged foods that are part of your normal diet and for which you have prices. Also, ensure that the across the set of food items there are positive values for each of the eight components of nutrition. Adjust the price for each food item so that it represents one serving size, as defined on the nutrition facts label. Each food item represents a decision variable in the linear programming problem.

The goal or objective of this problem is to find the minimum-cost diet (servings of food items) that satisfies the eight nutritional requirements. Use Python PuLP or AMPL (perhaps with its Python API). 

Deliverables (150 points total, 30 points for each part)

Paper (pdf file in GitHub repository). The paper/write-up should be submitted as a pdf file (two pages max for text, appendices for tables, figures, and images do not count in the two-page max). Think of the paper as comprising the methods and results sections of a written research report. If you like, provide a paragraph on methods and a paragraph about results for each of the five parts of this assignment. As this is an individual assignment about your personal eating habits, it is fine to use the first person in writing this paper. 

Program code (text link/URL to GitHub repository). Key information from the paper should also be included in the README.md markdown file of a public GitHub repository established by the student for this assignment. The GitHub repository should include text files for the program code, and program output, Image files (.jpg or .png extension) should be included for the scanned food labels may also be included in the repository. Include the web address text (URL) for the GitHub repository in the comments form of the assignment posting.  You should be providing a link to a separate repository that can be cloned. It should end with the .git extension.

This assignment has five graded components, with each component worth 30 points:

Part 1. Provide documentation for the five packaged food items you have selected for the assignment. Photographs of the Nutrition Facts labels are sufficient. Show your price calculations for serving sizes. 
Part 2. Specify the linear programming problem in standard form, showing decision variables, objective function with cost coefficients, and weekly nutritional constraints. Describe the problem in plain English. Implement the linear programming problem using Python PuLP or AMPL. Provide the program code and output/listing as plain text files, posting within a GitHub repository dedicated to this assignment. 
Part 3. Solve the linear programming problem using your Python PuLP or AMPL code. Describe the solution, showing units (serving sizes) for each of the five food items. What is the minimum cost solution? How much would you need to spend on food each week? Include the text file (listing) of your solution in the GitHub repository.
Part 4. Solutions to the diet problem are notorious for their lack of variety. Suppose you require at least one serving of each food item or meal during the week, setting constraints in the diet problem accordingly. Solve the revised linear programming problem. How do these additional constraints change the solution? How much more would you have to spend on food each week? Include the text file (listing) of your solution of this revised problem in the GitHub repository. Suppose this diet solution continues to lack variety. Describe how could you add further variety to your diet by making additional revisions to the model specification.
Part 5. Large language models (LLMs), as implemented with ChatGPT and other generative AI systems, are being used to solve many problems in data science. Select an LLM-based service or agent with which to work. Pick a free plan or one that is freely available to Northwestern students. (Do not pay for services in completing this assignment.) Indicate which service you have selected, providing its web address or uniform resource locator (URL). See if you can get your selected LLM agent to specify a model for The Diet Problem. See to what extent you can get the agent to develop computer code for The Diet Problem. Report on your success or failure. Provide a step-by-step review of your work. What prompts did you use? How did the conversation with the LLM agent go? Were you able to build on the conversation or to tailor it to your specific needs? As part of the GitHub repository for this assignment, include a plain text file of the complete conversation that you had with the LLM agent. Comment on your experience. Could an LLM agent be used to complete this assignment?

