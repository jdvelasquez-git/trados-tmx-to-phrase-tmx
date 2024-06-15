## 💭 Why this script?

Currently, [Phrase TMS](https://phrase.com/platform/tms/) doesn't provide an easy way via its UI to import Trados Studio TMX username metadata, specifically, from `created_by` and `changed_by` attributes. The same applies to `context` attributes.

If you are serious about your localization game, this is a clear problem because you want to know who translated what and who changed it last.

This script will help you with this by performing the following operations:

1. Move your username attributes inside the XML tree of your Trados Studio exported memories to a place Phrase TMS recognizes, including renaming these attributes to match Phrase's XML schema.
2. Print a list of all the usernames inside your Trados Studio translation memories. This will be useful because you will then pair it with the **UsernameXLtoTMX** script (see mapping section below).
3. Create updated TMX copies with the updated attributes.

## 📚 Instructions

First, you need to [install any stable Python version](https://www.python.org/downloads/) on your computer. This is especially true if you use Windows.

Once you install it, follow these steps:

### Trados TMX Update

1. Create language folders for each group of translation memories. For instance, if you work with 7 languages, you will create 7 folders and group them accordingly.
2. Jot down the ISO code of each language and its locale. You will need it during the conversion wizard.
3. Run the script.
4. It will ask you for a folder path. Start with your first folder.
5. Next, type the ISO code and locale (e.g., es-MX for Mexican Spanish). This will tell the script where to move the username attributes.
6. Hit Enter, and the script will begin creating updated TMX copies with the suffix __converted_.
7. Copy the list of usernames before exiting the script and paste it somewhere.

### Phrase Username Mapping 

Congratulations! You are one step away from the finish line. Now, we need to update your TMX usernames to match those you have created in Phrase. Follow these steps to finish:

1. Create an Excel file.
2. Name column A as `username`, and column B as `username_phrase`.
3. Paste the username lists from the script under column A.
4. Match each Trados Studio TMX username with your usernames in Phrase.
>  **This will be a painful, manual operation if you have hundreds, but there's no other way to match them.**
6. Save the Excel file and name it as "tmx_replace_list"
7. Move all your updated TMX files to a new folder together with the Excel file.
8. Open the replacementTool_ExcelToList script in Notepad.
9. Replace "sample.tmx" with the full name of your TMX file (there are two instances inside the script).
> **This is another manual process, but I will update the script to loop through all TMX files so you don't have to do this.**
10. Save your changes.
11. Run the script.

#### Important notes about using find and replace functions
If your Trados TMX usernames contain any characters such as "/\$.:^" please escape them with a backslash (\) inside the Excel file.

## 🧭 Updates Roadmap

- Merge the **replacementTool_ExcelToList** into the TMX conversion script. I will add some prompts to guide you through the process.
- Loop through all TMX files in the username mapping step.
- Transform Trados TMX `context` attributes to match Phrase XML schema.
