{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0a8c120a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "\n",
    "df = pd.read_csv('toy_dataset.csv')\n",
    "df\n",
    "\n",
    "X = list(df.iloc[:,3])\n",
    "Y = list(df.iloc[:,4])\n",
    "\n",
    "plt.bar(X, Y, color='black',width=0.25)\n",
    "plt.title(\"Age with Income\")\n",
    "plt.xlabel(\"Age\")\n",
    "plt.ylabel(\"Income\")\n",
    "plt.show()"
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
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
