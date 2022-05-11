{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "f8c77e72",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('red', 'blue', 'green', 'yello')\n",
      "Select your Option to perform tuple operation\n",
      " 1.View Tuple elements\n",
      " 2.Update\n",
      " 3.Frequency of element\n",
      " 4.Identify the index of ele\n",
      " 5.Length\n",
      " 6.Exit\n",
      " \n",
      "choice1\n",
      "You have selected View Tuple elements operation\n",
      "('red', 'blue', 'green', 'yello')\n",
      "choice2\n",
      "You have selected Update operation\n",
      "Enter the index\t3\n",
      "Enter the element to update\tbrown\n",
      "('red', 'blue', 'green', 'brown')\n",
      "choice2\n",
      "You have selected Update operation\n",
      "Enter the index\t2\n",
      "Enter the element to update\tbrown\n",
      "('red', 'blue', 'brown', 'yello')\n",
      "choice3\n",
      "You have selected Frequency of element operation\n",
      "('red', 'blue', 'green', 'yello')\n",
      "Enter the Element to check\n",
      "brown\n",
      "choice6\n",
      "You have selected Exiting---->>>> operation\n"
     ]
    }
   ],
   "source": [
    "def createTuple():\n",
    "    tup1=(\"red\",\"blue\",\"green\",\"yello\")\n",
    "    return tup1\n",
    "tup1=createTuple()\n",
    "print(tup1)\n",
    "def showTup(sho):\n",
    "    x\n",
    "    return tup1\n",
    "\n",
    "def updateTup(up):\n",
    "    y=list(tup1)\n",
    "    ind=int(input(\"Enter the index\\t\"))\n",
    "    ele=input(\"Enter the element to update\\t\")\n",
    "    y[ind]=ele\n",
    "    return y\n",
    "def countTup(coun):\n",
    "    ele=input(\"Enter the Element to check\\n\")\n",
    "    x=tup1.count(ele)\n",
    "    return x\n",
    "def indexTup(ind):\n",
    "    ele=input(\"Enter the element\")\n",
    "    x=tup1.index(ele)\n",
    "    return x\n",
    "def lenTup(len1):\n",
    "    x=len(tup1)\n",
    "    return x\n",
    "\n",
    "def tupOp(options):   \n",
    "    if choice==1:\n",
    "        select=\"View Tuple elements\"\n",
    "        print(f\"You have selected {select} operation\")     \n",
    "    elif choice==2:\n",
    "        select=\"Update\"\n",
    "        print(f\"You have selected {select} operation\")\n",
    "    elif choice==3:\n",
    "        select=\"Frequency of element\"\n",
    "        print(f\"You have selected {select} operation\")\n",
    "    elif choice==4:\n",
    "        select=\"Identify the index of ele\"\n",
    "        print(f\"You have selected {select} operation\")\n",
    "    elif choice==5:\n",
    "        select=\"Length\"\n",
    "        print(f\"You have selected {select} operation\")\n",
    "    elif choice==6:\n",
    "        select=\"Exiting---->>>>\"\n",
    "        print(f\"You have selected {select} operation\")\n",
    "    else:\n",
    "        print(\"Invalid input\")\n",
    "    return choice\n",
    "print(\"Select your Option to perform tuple operation\\n 1.View Tuple elements\\n 2.Update\\n 3.Frequency of element\\n 4.Identify the index of ele\\n 5.Length\\n 6.Exit\\n \")\n",
    "while True:    \n",
    "    choice=int(input(\"choice\"))\n",
    "    tupOp(choice)\n",
    "    if choice==1:\n",
    "        print(tup1) \n",
    "    elif choice==2:\n",
    "        print(tuple(updateTup(tup1)))\n",
    "    elif choice==3:\n",
    "        print(tup1)\n",
    "        countTup(tup1)\n",
    "    elif choice==4:\n",
    "        indexTup(tup1)\n",
    "    elif choice==5:\n",
    "        lenTup(tup1)\n",
    "    elif choice==6:\n",
    "        break\n",
    "    else:\n",
    "        print(\"!Wrong input!\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ab5ed754",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e625494b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "7f4ac2f3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('red', 'blue', 'green', 'yello')\n"
     ]
    }
   ],
   "source": [
    "def createTuple():\n",
    "    tup1=(\"red\",\"blue\",\"green\",\"yello\")\n",
    "    return tup1\n",
    "tup1=createTuple()\n",
    "print(tup1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "e1b95e51",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('red', 'blue', 'green', 'yello')"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def createTuple():\n",
    "    tup1=(\"red\",\"blue\",\"green\",\"yello\")\n",
    "    return tup1\n",
    "createTuple()"
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
