# Discord Bot Using GPT3.5 to Roleplay as Hanyuu from Higurashi no Naku Koro Ni

This discord bot responds to messages in all channels when the message starts with "hanyuu". More features are also present, which will be documented as they stabilize.

## Requirements

- A Discord bot
- An OpenAI account with some credits. Disclaimer: using GPT 3.5 is not free and consumes credit! Proceed with care.

## Usage

Install requirements: `pip install -r requirements.txt`

Create a file in the working directory called `secrets.json`, containing two fields:

- `DISCORD_API_KEY` containing the Discord bot's API key ;
- `OPENAI_API_KEY` containing your OpenAI API key.

Then, run `python hanyuu.py`. 

To run it as a daemon (in the background), you can run `tmux`, run `python hanyuu.py`, and then press Ctrl+D and B to detach. To attach to it again in the future, run `tmux a`.

The Discord bot will then reply to all messages starting with "Hanyuu". "hanyuu" in lowercase also works.

## Screenshots of results

TODO

## TODO

- Add an option to handle chat history - this was not implemented yet because it significally increases the OpenAI cost of queries. If you are interested in that, feel free to open an issue!