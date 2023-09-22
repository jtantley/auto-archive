# 📚 Markdown (.md) Notes <!-- omit from toc -->

📝 **Updated:** 08/09/2023.  
📓 **Personal reference document.**

---

## Contents <!-- omit from toc -->

- [Syntax](#syntax)
  - [Headers](#headers)
  - [Lists](#lists)
  - [Fenced code blocks](#fenced-code-blocks)
  - [Hyperlinks](#hyperlinks)
  - [Tables](#tables)
  - [Images](#images)
    - [Inline images](#inline-images)
    - [Responsive images](#responsive-images)
    - [Image captions](#image-captions)
    - [Image links](#image-links)
- [Emojis](#emojis)
  - [Emojis for project documentation](#emojis-for-project-documentation)
  - [List](#list)
  - [Arrows](#arrows)

---

## Syntax

### Headers

Headers: You can create headers with the following syntax:

```md
# This is a level 1 header

## This is a level 2 header

### This is a level 3 header

#### This is a level 4 header

##### This is a level 5 header

###### This is a level 6 header
```

---

### Lists

Lists: You can create lists with the following syntax:

```md
- This is an unordered list

  - This is a nested list
  - This is another nested list

- This is an ordered list
  1. This is the first item
  2. This is the second item
  3. This is the third item
```

---

### Fenced code blocks

You can show raw code in Markdown files by using fenced code blocks. To create a fenced code block, the code is enclosed by three backticks (`) on each side.

The language of the code block should be specified by adding a language name after the first backtick.

For example (Python):

    ``` python
      def factorial(n):
      if n == 0:
      return 1
      else:
      return n * factorial(n - 1)
    ```

---

### Hyperlinks

You can create links with the following syntax:

```md
[This is a link](https://www.google.com/)
```

---

### Tables

You can create tables with the following syntax:

```md
| Column 1       | Column 2             | Column 3               |
| -------------- | -------------------- | ---------------------- |
| This is a cell | This is another cell | This is the third cell |
```

---

### Images

You can embed images using the following syntax:

```md
![Alt text](image_path.jpg)
```

#### Inline images

You can embed an image inline with the following syntax:

```md
Inline image: ![Alt text](image_path.jpg)
```

This will display the image inline in the text of your Markdown file.

#### Responsive images

You can use responsive images with the following syntax:

```md
![Alt text](image_path.jpg){ width=400px }
```

This will display the image at a width of 400px. You can also specify the height of the image with the height attribute.

#### Image captions

You can add captions to images with the following syntax:

```md
![Alt text](image_path.jpg "Image caption")
```

This will display the image with the caption "Image caption" below the image.

#### Image links

You can create links to images with the following syntax:

```md
[![Alt text](image_path.jpg)](image_path.jpg "Image caption")
```

This will create a link to the image file. When the link is clicked, the image will be displayed.

&nbsp;

---

## Emojis

### Emojis for project documentation

**Changelog:**

- 🗒️: A notepad, representing the changes that have been made to the project.
- 📝: A pencil, representing the process of making changes to the project.
- 📑: A file folder, representing the different versions of the project.

**Project architecture:**

- 🏗️: A construction crane, representing the process of building the project.
- 🏢: A building, representing the finished project.
- 🗃️: A filing cabinet, representing the different components of the project.

**Directory structure:**

- 📂: A folder, representing the different directories in the project.
- 📁: A file, representing the files in the project.
- 📎: A paperclip, representing the connections between the different files and directories.

**Database structure:**

- 🗄️: A filing cabinet, representing the database tables.
- 📁: A file, representing the data in the database tables.
- 📄: A piece of paper, representing the queries that are used to access the data in the database tables.

**Backend:**

- 💻: A laptop computer, representing the hardware that is used to run the backend.
- 📡: A satellite dish, representing the network that is used to connect the backend to the frontend.
- ⚙️: A gear, representing the different components of the backend.

**Frontend:**

- 📱: A smartphone, representing the hardware that is used to run the frontend.
- 🖥️: A desktop computer, representing another type of hardware that is used to run the frontend.
- 🌐: A globe, representing the internet, which is used to connect the frontend to the backend.

**Features/functions:**

- 💡: A lightbulb, representing new ideas for features and functions.
- 🚀: A rocket, representing the launch of new features and functions.
- 🏆: A trophy, representing the success of new features and functions.

**LLM/NLP:**

- 🧠: A brain, representing the intelligence of LLM/NLP models.
- 💬: A speech bubble, representing the communication capabilities of LLM/NLP models.
- 🤖: A robot, representing the potential for LLM/NLP models to automate tasks.

**Tools:**

- 🛠️: A wrench and hammer, representing the tools that are used to build and maintain the project.
- 🔨: A hammer, representing the power of the tools that are used to build and maintain the project.
- ⚙️: A gear, representing the different components of the tools that are used to build and maintain the project.

**Libraries:**

- 📚: A bookshelf, representing the different libraries that are used in the project.
- 📖: A book, representing a specific library.
- 📓: A notebook, representing the documentation for a specific library.

**Integrations:**

- 🔌: A plug, representing the connection between the new component and the project.
- ➕: A plus sign, representing the addition of the new component to the project.
- 🛠️: A wrench and hammer, representing the work that is required to integrate the new component into the project.
- ⚙️: A gear, representing the different parts of the project that need to be adjusted to accommodate the new component.
- 🎛️: A control knob, representing the fine-tuning that may be required to get the new component working properly.
- 🏁: A checkered flag, representing the completion of the integration process.

**Directions:**

- 🛑 **Stop sign**: Indicates the end or a stopping point. Could be used to indicate where updates end and show the following documentation is outdated.

---

**Misc:**

- ✏️ Pencil
- 🔨 Hammer
- 🔧 Wrench
- 🔩 Nut and bolt
- 📯 Horn
- 🏆 Trophy, award

**Technology:**

- 📡 Satellite
- 💻 Computer, laptop
- 📱 Cell phone
- 📲 Cell phone call
- 📺 TV
- 📻 Radio
- ☎️ Telephone
- 📞 Phone receiver
- 📟 Pager
- 📠 Fax machine
- 📷 Camera
- 📹 Video camera, camcorder
- 🎥 Video camera, cinema
- 🎧 Headphones
- 🎤 Microphone
- 🔌 Electric plug
- 🔋 Battery

**Data storage:**

- 💾 Computer disk
- 💽 CD disk in case
- 💿 CD/DVD disk (gray)
- 📀 CD/DVD disk (gold)
- 📼 VHS tape

**Time:**

- 📆 Calendar with "31"
- 📅 Calendar with date marked
- ⌚ Watch
- ⏰ Alarm clock
- ⌛ Hour glass
- ⏳ Hour glass with flowing sand

**Papers:**

- 📚 Books, book stack
- 📖 Open book
- 📓 Notebook with speckled cover
- 📔 Notebook with decorative cover
- 📕 Red book
- 📙 Orange book
- 📗 Green book
- 📘 Blue book
- 📒 Ledger
- 📋 Clipboard
- 📄 Page
- 📃 Page with curl
- 📑 Page with bookmark tab
- 📝 Page with pencil, memo
- 📜 Scroll
- 📇 Card index
- 🔖 Bookmark
- 📰 Newspaper

**Graphs:**

- 📊 Bar graph
- 📈 Line graph, upwards trend, improvement
- 📉 Line graph, downwards trend

**Mail:**

- ✉️ Envelope
- 📨 Envelope incoming
- 📧 Email
- 📫 Mailbox (flag up, closed, new mail)
- 📬 Mailbox (flag up, open, new mail)
- 📪 Mailbox (flag down, closed, no new mail)
- 📭 Mailbox (flag down, open, empty)
- 📮 Postbox
- 📥 Inbox tray
- 📤 Outbox tray

**Lock:**

- 🔑 Key
- 🔒 Locked lock
- 🔓 Unlocked lock
- 🔐 Lock with key
- 🔏 Lock with ink pen

**Search:**

- 🔎 Search (facing right)
- 🔍 Search (facing left)

**Celebrate:**

- 🎉 Party, celebrate

**Hands:**

- 👋 Waving hand, hello
- 👍 Thumbs up, positive, +1
- 👎 Thumbs down, negative, -1
- 👆 Hand pointing up
- 👇 Hand pointing down
- 👈 Hand pointing left
- 👉 Hand pointing right
- ✌️ Hand showing peace sign
- 🖕 Hand showing middle finger
- 🙏 Thanks, praise
- 💪 Muscle, strong

**Nature:**

- ✨ Stars sparkling
- ⭐ Star
- 🌈 Rainbow
- ☀️ Sun
- ☁️ Cloud
- ❄️ Snowflake, cold
- 🌀 Cyclone
- ⚡ Lightning, zap
- ☔ Umbrella
- 🔭 Telescope
- 🌻 Sunflower

**X-Files:**

- 👽 Alien
- 💀 Skull, skeleton
- 🙈 Monkey see no evil
- 🙉 Monkey hear no evil
- 🙊 Monkey speak no evil

**Animals:**

- 🐺 Wolf
- 🐏 Sheep
- 🐸 Frog
- 🐷 Pig
- 🐔 Chicken
- 🐌 Snail
- 🐢 Turtle, tortoise
- 🐐 Goat
- 🐇 Rabbit
- 🐟 Fish
- 🐄 Cow
- 🐊 Crocodile, alligator

**Faces:**

- 😕 Confused, unsure

**Abstract:**

- 💥 Explosion, boom, collision
- 🎶 Music notes
- 💤 Sleep
- 💭 Thought bubble

**Moon:**

- 🌔 Moon
- 🌑 New moon
- 🌒 Waxing crescent moon
- 🌓 First quarter moon
- 🌔 Waxing gibbious moon
- 🌕 Full moon
- 🌖 Waning gibbous moon
- 🌗 Last quarter moon
- 🌘 Waning crescent moon
- 🌜 Crescent moon facing right
- 🌛 Crescent moon facing left

**Symbols:**

- 🔛 "On" sign
- 🔜 "Soon" sign
- 🔚 "End" sign
- 🚫 No entry, circle crossed out
- ⛔ No entry, red circle with horizontal line
- ✳️ Asterisk on green background
- ☑️ Checkmark on blue background
- 🔘 Radio button
- ⭕ Red circle, red ring on transparent background
- ⚫ Black circle
- ⚪ White circle
- 🔴 Red circle
- 🔵 Blue circle
- 🔶 Red diamond
- 🔷 Blue diamond
- ✖️ Multiplication symbol
- ➕ Plus symbol, addition
- ➖ Minus symbol, subtraction
- ➗ Division symbol
- ❕ Exclamation point (gray)
- ❔ Question mark (gray)

---

### List

- 📌️ **Pin:** Often used to represent a bullet point to make a note stand out in the text. Can be used to to indicate project version.

- ⚠️ **Warning:** Used to indicate a warning or caution.
- 🚧 **Under construction:** Used to indicate that something is still under development.
- 👷 **Worker:** Used to represent someone who is working on something.
- 🏗️ **Construction crane:** Represents the process of building a dev project.
- 📝 **Pencil over paper:** Can represen the process of making changes to the project.
- 🗒️ **Yellow notepad:** Can represent a changelog or changes that have been made to the project.

- 🔜 **Soon:** Used to indicate that something is coming soon.
- 🏢 **Building:** Used in project achitecture to represent a finished project.
- 🚀 **Ready to go:** Used to indicate that something is ready to be used.

- 🔨 **Code update:** Can be used to show that project code has been updated.
- 💡 **Info/Tip:** Used to indicate tips, advice, and helpful information.
- ⚙️ **Gear:** Can represent the different components of the backend.
- 🔑 **Key:** Often used to represent access, security, or knowledge, including account credentials and API keys

- ✨ **New feature:** Can be used to announce new project features.
- 🔎 **Magnifying glass:** Often used to represent search or a search feature/function.
- 💬 **Chat:** Used to represent a chat bubble, often to represent communication/collaboration. Can also be used to represent a chat feature/function.
- 📚 **Book:** Used to represent a book, which is often used as a symbol for knowledge or research.
- 📖 **Open book:** Often used to represent a reference document that is being used, as it specifically indicates an open book.
- 📓 **Notebook:** Used to represent a notebook, often a symbol for notes or research. Sometimes used to represent a 'to-do' list.

- 🗃️ **Folder/File cabinet:** This emoji is commonly used to represent a folder or file directory.
- 📁 **Folder/File:** This emoji is usually used to represent a folder or file.

- 📄 **Document:** Can be used to represent any type of document.
- 📝 **Documentation:** Useful for indicating that the documentation for the project has been updated.
- 📃 **Miscellaneous:** Catch-all emoji for any other kind of documentation update.
- 🗄️ **Database/File stack:** Often used to represent a database or large amount of data or files.

- 📨 **Inbox:** Used to represent an inbox, which is often used to represent incoming messages or notifications.
- 📤 **Outbox:** Used to represent an outbox, which is often used to represent outgoing messages or notifications.

- 🔗 **Link:** Sometimes used to represent an attachment, as it is a symbol for a hyperlink.
- 📎 **Paperclip:** Often used to represent an attachment, as it is a symbol for holding things together.

- 🤖 **Robot:** Often used to represent artificial intelligence (AI) or robots.
- 👩‍💻 **Data Scientist:** Often used to represent computer scientists or software engineers.
- 🕵️‍♂️ **Detective:** Often used to represent data scientists or machine learning (ML) engineers.

- 🧠 **Brain:** Often used to represent intelligence or thought.
- 🧪 **Experiment:** Often used to represent experimentation or research.

- 💻 **Computer:** Used to represent a computer.
- 🖥️ **Desktop:** Used to represent a desktop computer.
- ⌨️ **Keyboard:** Used to represent a keyboard and keyboard shortcuts.
- 🖱️ **Mouse:** Used to represent a mouse.
- 📡 **Satellite:** Often used to represent the internet or cloud computing.
- 🌐 **Globe:** Often used to represent the internet, a digital ecosystem, or a a global nature.
- 💾 **Hard drive:** Often used to represent a storage or data or to represent a backup or a copy of data.

- 🗜️ **Compress:** Often used to represent compression or the process of reducing file size.

- 🗳️ **Poll:** Often used to represent a poll or a survey.
- 📊 **Chart:** Often used to represent a chart or a graph.
- 📈 **Improvement:** Often used to represent an improvement/increase or a trend/pattern.
- 📉 **Decline:** Often used to represent a decline/decrease.

- 🔱 **Competition:** Often used to represent competition or rivalry.
- 🏆 **Award:** Often used to represent an award or recognition.
- 🎉 **Celebration:** Often used to represent celebration or a happy occasion.

- ✅ **Check:** Used to indicate that something has been checked or verified.
- ❌ **Cross:** Used to indicate that something has been crossed out or is not correct.
- ❓ **Question:** Used to indicate a question.
- ❗️ **Important:** Used to indicate something that is important.

- ⌛ **Sand timer:** Used to represent time passing.

&nbsp;

---

&nbsp;

**Emoji sequences:**

- 📁📂📃: This sequence of emojis can be used to represent a stack of documents.
- ⏳⏳⏳: This sequence of emojis can be used to represent a countdown timer.
- 🗄️📁: This combination of emojis is often used to represent file storage.
- 📡🌐: This combination of emojis is often used to represent the internet and the web
- 🧪📓 - Experiment and to-do list
- 💾🗜️ - Backup and compression
- 🗳️📊 - Poll and chart
- 📈📉📈 - Trend, decline, and improvement
- 🔱🏆🎉 - Competition, award, and celebration

&nbsp;

---

&nbsp;

**Custom Emoji Sequences:**

You can use combinations of emojis to create your own sequences that are specific to your project's needs.

For example, if your project is about artificial intelligence, you might use the following sequence:

- 🤖💻🗄️🌐: AI, computer, database, the web

&nbsp;

---

### Arrows

**ASCII characters:**

- ^: Up arrow
- ↑: Up arrow
- ↗: Upwards pointing right arrow
- ↖: Upwards pointing left arrow
- ⇈: Double upwards pointing arrow
- ⇊: Double downwards pointing arrow

**Emojis:**

- ⬆️: Upward black arrow
- ↗️: Upward right arrow
- ↑: Upward arrow
- ↖️: Upward left arrow
- ⤴️: Upward curved arrow
- 🔼: Upwards button
- 📐: Triangular ruler pointing upwards

**Emojis for file versions:**

- 💾: A floppy disk, which is a symbol of saving files.
- 📁: A folder, which is a symbol of storing files.
- 📝: A pencil, which is a symbol of editing files.
- 🔱: A trident, which is a symbol of power and authority.
- 🕑: A clock, which is a symbol of time and updates.
- 🚀: A rocket, which is a symbol of progress and improvement.
- ⬆️: An arrow pointing up, which is a symbol of positive change.
- 🆕: A new symbol, which is a symbol of freshness and innovation.
- 💯: A hundred points, which is a symbol of perfection and excellence.
- 🏆: A trophy, which is a symbol of achievement and success.

> **Bard (08/18/23):** "You can also use a combination of emojis to create a more specific representation of a file version. For example, you could use the 📁 emoji (folder) and the 📝 emoji (pencil) to represent a file version that has been edited. Or, you could use the 🔱 emoji (trident) and the 🚀 emoji (rocket) to represent a file version that is a major update."
>
> > - 📁📝
> > - 🔱🚀
>
> &nbsp;

**Emojis for Python project README file:**

- 🐍: A snake, which is a symbol of Python.
- 💡: A light bulb, which is a symbol of creativity and innovation.
- 💻: A computer, which is a symbol of technology and programming.
- 📚: A book, which is a symbol of knowledge and learning.
- ✨: A sparkle, which is a symbol of awesomeness and excitement.
- ⭐️: A star, which is a symbol of excellence and achievement.
- 💯: A hundred points, which is a symbol of perfection and excellence.
- 🏆: A trophy, which is a symbol of achievement and success.
- 🤝: A handshake, which is a symbol of collaboration and teamwork.
- 🎉: A party popper, which is a symbol of celebration and joy.

**Emojis for data-related sections:**

- 📊: A bar chart, which is a symbol of data visualization.
- 📈: A line chart, which is another symbol of data visualization.
- 📉: A declining line chart, which could be used to represent a decrease in data.
- 📈: An increasing line chart, which could be used to represent an increase in data.
- 💾: A floppy disk, which is a symbol of storing data.
- 📁: A folder, which is a symbol of organizing data.
- 💻: A computer, which is a symbol of processing data.
- 🖨: A printer, which is a symbol of printing data.
- 📲: A mobile phone, which is a symbol of accessing data on the go.
- 🌐: A globe, which is a symbol of global data.
- 🗺: A map, which is a symbol of geographical data.

> **Bard (08/18/23):** "You can also use emojis to represent specific data types. For example, you could use the 🔢 emoji (number) to represent numerical data, or the 🔠 emoji (alphabet) to represent textual data."
>
> &nbsp;

---
