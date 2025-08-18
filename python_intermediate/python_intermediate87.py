Introduction
In the last lesson, we learned to organize our code using modules. In addition to modules, packages help us to further divide a large project into smaller components.

Suppose we are developing a large project. To simplify this project, we can first divide the project into modules.

If our program is very large, there might be a lot of these modules. So, we further need to group related modules together so that everything is organized. Python packages allow us to do just that. Packages help us to organize related modules together.

Practical Scenario
Suppose we are developing a game with multiple objects, so it may have these different modules.

player.py
boss.py
gun.py
knife.py
If we put all these modules in the same directory, they look cluttered. In such scenarios, we can use packages to structure them.

Organization of code in Python packages.
Figure: Python Packages to Organize Files
Here,

The similar modules player and boss are kept inside the characters package.
Similarly, gun and knife modules are kept inside the weapons package.
And, character and weapons packages are kept inside the game package.
As you can see, our project looks much more organized and structured with the use of packages.

Confused about something? Ask a question!
