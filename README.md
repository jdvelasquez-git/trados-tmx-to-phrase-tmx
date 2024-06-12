## 💭 Why this script?

Currently, Phrase doesn't provide any way you can read Trados Studio TMX username metadata, specifically, from **creation** and **change** attributes.

If you are serious about your localization game, this is a clear problem because you want to know who translated what and who changed it last.

This script will help you exactly with that:

1. It will move your username attributes inside the XML tree of your Trados Studio exported memories to a place Phrase recognizes.

2. It will give you a list of all the usernames inside your translation memories. This will be useful because you will then pair it with another script.

3. It will perform this operation in the target language of your preference.

## 📚 Instructions

First, you need to install any stable Python version on your computer. This is especially true if you use Windows. You can download it from the [official website]([url](https://www.python.org/)).

Once you install it, follow these steps:

1. Create language folders for each group of translation memories. For instance, if you work with 7 languages, you will create 7 folders and group them accordingly.
2. Jot down the ISO code of each language and its locale. You will need it during the conversion wizard.
3. Run the script.
4. It will ask you for a folder path. Start with your first folder.
5. Next, type the ISO code and locale (e.g., es-MX for Mexican Spanish). This will tell the script where to move the username attributes.

The script will start to work and give you lists of usernames for each valid TMX file. Meanwhile, it will generate updated TMX copies with the suffix __converted_.

That's it!

## 🧭 Improvements

If there's enough interest, the next improvement to this script would be to transform the context attributes so that Phrase can leverage them. Let me know! 😉
