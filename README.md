# Chat-bot-Evaluation-Project
Chat-bot evaluation project resources for the Grapevine High School Science Fair in January 2018. In order to ensure that test subjects remain anonymous, the names of people from the original samples are not included.
# Key
chatbot_answers.txt: answers given by the chat-bot in response to the questions from the stratified random sample.<br>
comparison.py: the platform used during the test to input the evaluations of the four judges.<br>
deep.txt: conversation starters from https://conversationstartersworld.com/deep-conversation-topics/.<br>
get_to_know.txt: conversation starters from https://conversationstartersworld.com/questions-to-get-to-know-someone/.<br>
good_questions.txt: conversation starters from https://conversationstartersworld.com/good-questions-to-ask/.<br>
ground_answers.txt: responses recorded from humans to compare against the responses of the chat-bot.<br>
philosophical.txt: conversation starters from https://conversationstartersworld.com/philosophical-questions/.<br>
question_sample.txt: the 40 questions sampled using a stratified random sample from the total population of 1089 conversation starters (combination of deep.txt, get_to_know.txt, good_questions.txt, philosophical.txt, and starters.txt).<br>
reformatted_chatbot_answers.txt: reformatted version of chatbot_answers.txt (used in comparison.py).<br>
reformatted_ground_answers.txt: reformatted version of ground_answers.txt (used in comparison.py).<br>
roll.py: the script that samples questions from the total population of 1089 conversation starters and samples the judges using a simple random sample.<br>
starters.txt: conversation starters from https://conversationstartersworld.com/250-conversation-starters/.<br>
<br>
# Requirements
#### Numpy 1.13.3+
#### Tensorflow 1.3.0 + 
#### Natural Language Toolkit 3.2.4+
```batch
python -m pip install --upgrade numpy tensorflow nltk
```
## Synopsis
40 conversation starters are sampled using a stratified random sample from the aggregate produced by appending deep.txt, get_to_know.txt, good_questions.txt, philosophical.txt, and starters.txt. 
```batch
python roll.py sample_questions
```
The artificial chat-bot responses to these questions are recorded by feeding them into the Deep Q&A chat-bot and writing its exact responses in chatbot_answers.txt. The "ground truth" human responses to these questions are recorded by sampling five people from the 6th period Superchemistry class (names were listed in omitted class.txt file) using a simple random sample and asking each participant to respond to eight of the 40 questions. Every person who participated gave verbal consent and was debriefed afterwards.
```batch
python roll.py sample_ground
```
When it is time to conduct the study, judges are sampled from the file class.txt.
```batch
python roll.py sample_judges
```
The four judges were led to an isolated room where they completed the study using comparison.py. They were given the objective of determining the answer to the question that "is the most appropriate." Verbal consent was given by all four judges from the three simple random samples conducted to both having their responses recorded and working with the group of people. Afterwards, all judges were debriefed because they have prior knowledge of the purpose of the study.
```batch
python comparison.py
```
One person who is not a judge interprets the responses from the judges. If the judges strongly agree that one answer is more appropriate than another answer, then 1+ or 2+ is recorded, whereby the number corresponds to the chosen more appropriate answer. If the judges agree that one answer is more appropriate than another answer but there is some disagreement or equivocation, then a 1 or 2 is recorded, whereby the number corresponds to the chosen more appropriate answer. If there is no agreement between the judges, then a 0 is recorded. These recordings are translated by the program into scores. This system is inspired by the implementation of human evaluation done by Li et al. in <i>A Persona-Based Neural Conversation Model</i>.
#### Scores Key
+2 is scored if the human answer is confidently identified.<br>
+1 is scored if the human answer is equivocally identified.<br>
0 is scored if the judges cannot agree on a single answer.<br>
-1 is scored if the chat-bot answer is equivocally identified.<br>
-2 is scored if the chat-bot answer is confidently identified.<br>
### More Implementation Notes
I input and interpretted the decisions for the judges. In order to minimize bias introduced, I could not clarify the meaning of responses (i.e., answer what each response means) and abstained from commenting. The only thing that I clarified was specific vocabulary (e.g., the meaning of the word dystopia). The chat-bot curses in one of its responses; to remove the unnecessary offense created by this, I censored it when formatting the responses of the chat-bot. 
# Results
Using a chi-square test and significance value of alpha=0.005, the null hypothesis, corresponding to the chat-bot being indistinguishable, is rejected twice, but is failed to be rejected once. Qualitatively, a common fail-case is the chat-bot giving nonsensical replies, which corresponds to a failure to interpret the question. Persiyanov, Dmitry (2017) identifies this difficulty with language as common in generative NLP models.
<br>
# Bibliography
Abadi, Martín et al. "TensorFlow: A system for large-scale machine learning." 12th USENIX Symposium on OSDI, 2016, https://arxiv.org/abs/1605.08695.<br>
Bird, Steven, et al. Natural Language Processing with Python. O'Reilly, 2011.<br>
Daniels, C. B. “Conversation Starters World.” Conversation Starters World, 2017, conversationstartersworld.com/.<br>
Hugunin, Jim.  "The Python Matrix Object: Extending Python for Numerical Computation." Proceedings of the Third Python Workshop, Reston, Va., Dec. 1995, http://legacy.python.org/workshops/1995-12/papers/hugunin.html.<br>
Li, Jiwei et al. "A Persona-Based Neural Conversation Model." Association for Computational Linguistics, 2016, https://arxiv.org/abs/1603.06155.<br>
Persiyanov, Dmitry. "Chatbots with Machine Learning: Building Neural Conversational Agents." Stats and Bots, Sept. 2017, https://blog.statsbot.co/chatbots-machine-learning-e83698b1a91e<br>
Pot, Etienne, Deep Question and Answer, 2017, GitHub repository, https://github.com/Conchylicultor/DeepQA.<br>
Vinyals, Oriol, and Quoc V. Le. "A Neural Conversational Model." International Conference on Machine Learning, vol. 37, 2015. https://arxiv.org/abs/1506.05869.<br>
