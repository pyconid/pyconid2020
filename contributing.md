# Contributing to Pycon Indonesia 2020 Website

When contributing to this repository, please first discuss the change you wish to make via [issue](https://github.com/pyconid/pyconid2020/issues),
email, or any other method with the maintainers of this repository before making a change. 

>Please note we have a code of conduct, please follow it in all your interactions with the project.

## Pull Request Process
Pull requests are the best way to propose changes to the codebase (we use [Github Flow](https://guides.github.com/introduction/flow/index.html)). We actively welcome your pull requests:

1. Fork the repo and create your branch from `develop`.
2. If you've added code that should be tested.
3. If you've changed/added some APIs, update the documentation.
4. Make sure your code lints.
6. Issue that pull request!

## Contribute Guidelines

### Project Structure
Here the project structure for pycon id 2020 website.
```
PyconID 2020
│   README.md
|   pelicanconf.py
|   Makefile    
|   ...
│
└───content
│   │
│   └───pages
│   |   │   speakers.md
│   |   │   sponsor.md
|   |   |   blog.md
│   |   │   ...
│   |
│   └───articles
|   |   |   example_article.md
|   |   |   ...
|   |
│   └───speakers (soon)
|
└───themes
    |
    └───eventtalk
        |
        └───static
        |   |
        |   └───css
        |   |
        |   └───js
        |   |
        |   └───img
        |
        └───templates
            |   base.html
            |   blog.html
            |   speakers.html
            |   sponsor.html
            |   ...
        
```

### Add / Update Website Content/Page
You can create a new content/page for this website by following the steps below.

1.  Create new markdown file in ```content/pages```.
2.  Don't forget to declare ```title```, ```template```, and ```slug``` first in the markdown file before you write your content.
3. You can use ```general.html``` template or create your own template in ```themes/eventalk/templates```, but if you create a new template, don't forget to update the documentation.
4. Done.
5. See [Call for Paper](https://raw.githubusercontent.com/pyconid/pyconid2020/develop/content/pages/call-for-paper.md)

### Create / Update Article
Creating new article, follow the steps below.
1. Create new markdown file in ```contents/articles```.
2. make sure you are already declaring these variable before create article content:

    + ```title```, Page/Article title, eg: Pycon Indonesia 2020 has begun.

    + ```Template```, use ```blog-single``` template to create an article.

    + ```author```, Author of this article, eg: Chitoge Kirisaki or Someone. 

    + ```date```, Date created, the date format must be DD-MM-YYYY HH:mm ```Not Hhmm......``` just kidding :D.

    + ```category```, Not a important thing, but just add it, eg: Artificial Intelegence or GIS or something.

    + ```slug```, Slug URL, eg: welcome-to-pycon-id-2020.

    + ```image```, image banner & thumbnail for this article, eg: pycon.jpeg , save the image in ```static/img/blogs``` directory.

3.  See : [Sample Article](https://raw.githubusercontent.com/pyconid/pyconid2020/develop/content/articles/article-one.md)

4. After creating article markdown file, don't forget to register your article to ```articles``` variable in ```content/pages/blog.md```. 

5. Use this following pattern to add your article in ```articles``` variable ```Title~Author~DateCreated~Slug~ImageThumbnail```, eg:  ```Welcome to PyCon ID 2020~Adif Dwi Maulana~08-08-2020 14:11:12~welcome-to-pycon-id-2020~1.JPG```

6. Done

### Add / Update Speakers
Soon

## Code of Conduct
### Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, gender identity and expression, level of experience,
nationality, personal appearance, race, religion, or sexual identity and
orientation.

### Our Standards

Examples of behavior that contributes to creating a positive environment
include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or
advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic
  address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

### Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

### Scope

This Code of Conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community. Examples of
representing a project or community include using an official project e-mail
address, posting via an official social media account, or acting as an appointed
representative at an online or offline event. Representation of a project may be
further defined and clarified by project maintainers.

### Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting the project team at [INSERT EMAIL ADDRESS]. All
complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. The project team is
obligated to maintain confidentiality with regard to the reporter of an incident.
Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.

### Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4,
available at [http://contributor-covenant.org/version/1/4][version]

[homepage]: http://contributor-covenant.org
[version]: http://contributor-covenant.org/version/1/4/