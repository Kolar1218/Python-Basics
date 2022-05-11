{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "47d29e17",
   "metadata": {},
   "outputs": [],
   "source": [
    "quiz_question = {\"Question 1\":{\"Question\":\"In which language is Python written?\",\"Option1\": \"Java\",\"Option2\": \"C++\",\"Option3\": \"C\",\"Correct answer\": \"C\"},\n",
    "              \"Question 2\":{\"Question\":\"How is a code block indicated in Python?\",\"Option1\": \"Indentation\",\"Option2\": \"Loops\",\"Option3\": \"Key\",\"Correct answer\": \"Indentation\"},\n",
    "              \"Question 3\":{\"Question\":\"What will be the result of the following expression  “2 ** 3 + 5 ** 2”?\",\"Option1\": \"33\",\"Option2\": \"29\",\"Option3\": \"31\",\"Correct answer\": \"33\"},\n",
    "              \"Question 4\":{\"Question\":\"What will be the output of the following code print(5**3 + (3 + 6)**(2 + 0))\",\"Option1\": \"155\",\"Option2\": \"107\",\"Option3\": \"156\",\"Correct answer\": \"156\"},\n",
    "              \"Question 5\":{\"Question\":\"Which of the following concepts is not a part of Python?\",\"Option1\": \"Loops\",\"Option2\": \"Operators\",\"Option3\": \"Pointers\",\"Correct answer\": \"Pointers\"},\n",
    "              \"Question 6\":{\"Question\":\"Which of the following is the proper syntax to check if a particular element is present in a list?\",\"Option1\": \"if ele in list\",\"Option2\": \"if not ele not in list \",\"Option3\": \"Both\",\"Correct answer\": \"Both\"},\n",
    "              \"Question 7\":{\"Question\":\"Which data structure in python store only unique elements within them, without any repetition\",\"Option1\": \"Tuple\",\"Option2\": \"Set\",\"Option3\": \"Dict\",\"Correct answer\": \"Set\"},\n",
    "              \"Question 8\":{\"Question\":\"Which functions converts date to corresponding time in Python?\",\"Option1\": \"striptime()\",\"Option2\": \"timestrip()\",\"Option3\": \"datetime()\",\"Correct answer\": \"striptime()\"},\n",
    "              \"Question 9\":{\"Question\":\"Which data structure is a combination of Keys and value pairs\",\"Option1\": \"Set\",\"Option2\": \"List\",\"Option3\": \"Dictionary\",\"Correct answer\": \"Dictionary\"},\n",
    "              \"Question 10\":{\"Question\":\"Select the flow of exception handlig \",\"Option1\": \"try,except,finally\",\"Option2\": \"try,finally,except\",\"Option3\": \"finally,try,except\",\"Correct answer\": \"try,except,finally\"},\n",
    "              \"Question 11\":{\"Question\":\"What keyword is used in Python to raise exceptions?\",\"Option1\": \"try\",\"Option2\": \"raise\",\"Option3\": \"catch\",\"Correct answer\": \"raise\"},\n",
    "              \"Question 12\":{\"Question\":\"Identify the output of the following round(1.571)\",\"Option1\": \"1\",\"Option2\": \"2\",\"Option3\": \"1571\",\"Correct answer\": \"2\"},\n",
    "              \"Question 13\":{\"Question\":\"All keywords in python are\",\"Option1\": \"lower case\",\"Option2\": \"Upper case\",\"Option3\": \"Case sensitive\",\"Correct answer\": \"Case sensitive\"},\n",
    "              \"Question 14\":{\"Question\":\"What is the return type of id()\",\"Option1\": \"float\",\"Option2\": \"string\",\"Option3\": \"int\",\"Correct answer\": \"int\"},\n",
    "              \"Question 15\":{\"Question\":\"The format function when applied on a string returns\",\"Option1\": \"int\",\"Option2\": \"str\",\"Option3\": \"float\",\"Correct answer\": \"str\"},\n",
    "              \"Question 16\":{\"Question\":\"In which year was the Python 3.0 version developed?\",\"Option1\": \"2008\",\"Option2\": \"2010\",\"Option3\": \"1998\",\"Correct answer\": \"1978\"},\n",
    "              \"Question 17\":{\"Question\":\"Which of the following is a tuple in python\",\"Option1\": \"{1,2,3}\",\"Option2\": \"[1,2,3]\",\"Option3\": \"(1,2,3)\",\"Correct answer\": \"(1,2,3)\"},\n",
    "              \"Question 18\":{\"Question\":\"Which of the following is floor division \",\"Option1\": \"\\\\\",\"Option2\": \"\\/\",\"Option3\": \"//\",\"Correct answer\": \"//\"},\n",
    "              \"Question 19\":{\"Question\":\"Which one is not keyword in python\",\"Option1\": \"else\",\"Option2\": \"if\",\"Option3\": \"string\",\"Correct answer\": \"string\"},\n",
    "              \"Question 20\":{\"Question\":\"The maximum length of the python identifier is\",\"Option1\": \"31 Chars\",\"Option2\": \"32 Chars\",\"Option3\": \"16 Chars\",\"Correct answer\": \"31 Chars\"},\n",
    "              \"Question 21\":{\"Question\":\"String is PYTHON, what is the output of the code print(s[-1:3])\",\"Option1\": \"ON\",\"Option2\": \"No\",\"Option3\": \"no\",\"Correct answer\": \"ON\"},\n",
    "              \"Question 22\":{\"Question\":\"which one of the following has the highest precedence in the expression\",\"Option1\": \"Addition\",\"Option2\": \"Multiplication\",\"Option3\": \"Parentheses\",\"Correct answer\": \"Parentheses\"},\n",
    "              \"Question 23\":{\"Question\":\"In which year was the Python language developed?\",\"Option1\": \"1989\",\"Option2\": \"1999\",\"Option3\": \"1979\",\"Correct answer\": \"1989\"},\n",
    "              \"Question 24\":{\"Question\":\"Which one of the following is the correct extension of the Python file?\",\"Option1\": \".python\",\"Option2\": \".py\",\"Option3\": \".p\",\"Correct answer\": \".py\"},\n",
    "              \"Question 25\":{\"Question\":\"What is the method inside the class in python language?\",\"Option1\": \"Function\",\"Option2\": \"Class\",\"Option3\": \"Object\",\"Correct answer\": \"Function\"}}"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
