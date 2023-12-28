install:
		awk 'BEGIN {print "#! /usr/bin/env python3"} 1' chatbot.py > chatbot && \
		chmod +x chatbot && \
		mv chatbot ~/.local/bin/chatbot
