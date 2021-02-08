{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import pickle as pkl\n",
    "\n",
    "A = pd.read_excel(\"/Users/ashish/OneDrive/Desktop/Deployment/Start.xlsx\")\n",
    "\n",
    "X = A[['RND','MKT']]\n",
    "Y = A[['PROFIT']]\n",
    "\n",
    "from sklearn.linear_model import LinearRegression\n",
    "\n",
    "lm = LinearRegression()\n",
    "model = lm.fit(X,Y)\n",
    "\n",
    "pkl.dump(model,open(\"model.pkl\",\"wb\"))\n",
    "model = pkl.load(open(\"model.pkl\",\"rb\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
