# Quadratic Solver

#### Video Demo: [Click Here for a Demo!](https://youtu.be/rzInRpNzjhw)

#### Description:
The Quadratic Solver is an interactive educational tool designed to teach users about various methods for solving quadratic equations and to provide a calculator for solving these equations. This web app covers different approaches such as graphing, factoring, completing the square, and using the quadratic formula. It allows users to practice and solve quadratic equations interactively.

## Project Structure

### Template Files

#### `index.html`
This is the main entry point of the web app. It provides an overview of the app and guides users to different sections where they can learn about different methods for solving quadratic equations. It provides easily accessible links to the other pages in the web app.

I decided not to include a login page to make it more accessible.

#### `apology.html`
This template is used to display error messages or apologies when something goes wrong or if a requested page is not found.

#### `calculator.html`
This template provides the interactive calculator where users can input the coefficients of a quadratic equation and get the solutions using the quadratic formula. It includes fields for entering the values of \(a\), \(b\), and \(c\), and a button to calculate the roots.

I was able to utilize python and jinja logic to enable a "step-by-step" solution that teaches students how to go through the problem. Additionally, I have embedded a Desmos interactive calculator that points out the roots through a visual metric for visual learners.

#### `completing_the_square.html`
This template explains the method of solving quadratic equations by completing the square. It includes a step-by-step guide and examples to help users understand this technique.

#### `factorizing.html`
This template covers the method of solving quadratic equations by factorizing. It provides detailed explanations and examples of how to factorize quadratic equations to find their roots.

#### `graphing.html`
This template demonstrates how to solve quadratic equations by graphing. It includes information on plotting the graph of a quadratic equation and finding the roots visually.

#### `quadratic_formula.html`
This template explains the quadratic formula method for solving quadratic equations. It provides the formula, detailed steps for using it, and examples to illustrate the process.

### `styles.css`
This CSS file contains the styles for the web app, ensuring a clean and user-friendly interface. It includes styles for:

- Page layout and structure
- Typography and colors
- Interactive elements like buttons and input fields
- Responsive design to ensure the app works well on different devices

#### `layout.html`
This is the layout template that contains the common structure for all pages, including the header, footer, and navigation bar. Other templates extend this layout to maintain a consistent look and feel across the web app.

### `README.md`
This Markdown file contains the educational content for the web app. It includes detailed explanations, examples, and practice problems for each method of solving quadratic equations. The content is structured to be easy to read and understand, with clear headings and subheadings.

## Usage

To use Quadratic Solver, follow these steps:

to create a new environment, run:
```console
python -m venv env
source env/bin/activate
```

in this new environment, run:
```console
pip install flask
pip install flask_session
```

to run out of the box, in ```folynomials/```, run:
```console
flask run
```

to edit your local version and see changes, in ```folynomials/```, run:
```console
flask --app app.py --debug run
```

### Example
To solve the quadratic equation \(x^2 - 3x + 2 = 0\) using the calculator:

1. Enter `1` in the `a` field.
2. Enter `-3` in the `b` field.
3. Enter `2` in the `c` field.
4. Click the "Solve" button to get the roots.

The calculator will display the roots: `2` and `1`.

### Educational Focus
The primary goal of this web app is to educate users about different methods for solving quadratic equations. Each method is explained in detail with examples, allowing users to understand the underlying concepts and techniques.

### Interactive Learning
The web app includes interactive elements such as the calculator and practice problems, providing users with a hands-on learning experience. This helps reinforce the concepts learned in the educational sections.

### User-Friendly Interface
The design of the web app is clean and user-friendly, ensuring that users can easily navigate through the content and use the calculator. The responsive design ensures that the app works well on various devices, including desktops, tablets, and smartphones. Additionally, I used LaTeX-like formatting for the numbers to make it less cryptic, as well as developed a method to include interactive Desmos calculators. I have also implemented a favicon for users to quickly navigate through their tabs bar, as well as ensure a more friendly interface.

## Future Improvements

There are several potential improvements that could be made to this project:

1. **Enhanced Content**: Adding more detailed explanations, additional examples, and practice problems for each method.
2. **Advanced Calculator Features**: Extending the calculator to handle complex roots and provide step-by-step solutions.
3. **User Feedback**: Incorporating user feedback to continuously improve the educational content and interactive features.

## Conclusion

The Quadratic Solver is a comprehensive educational tool that provides users with the knowledge and tools to solve quadratic equations using different methods. It combines detailed explanations with interactive elements to create an engaging learning experience.

For any questions or suggestions, please feel free to reach out!
