{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOI+PW9cAKy3NdRv+jB3Szs",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/esrasucu/miniOrumcek/blob/main/dataURL.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "aip8NP247B8X"
      },
      "outputs": [],
      "source": [
        "class DataURL:\n",
        "  dataFile = \"dataURL.txt\"\n",
        "\n",
        "  def __init__(self):\n",
        "    fileTest = open(self.dataFile, \"a\")\n",
        "    self.data = fileTest.read()\n",
        "    fileTest.close()\n",
        "\n",
        "  def dataWrite(self):\n",
        "    dataOpen = open(self.dataFile, 'a')\n",
        "    siteURL= input(\"Site adresini ön eki ile birlikte giriniz: \")\n",
        "    dataOpen.write(siteURL+ \"/n\")\n",
        "    dataOpen.close()\n",
        "\n",
        "  def dataRead(self):\n",
        "    dataOpen = open(self.dataFile, 'r')\n",
        "    for dataShow in dataOpen:\n",
        "      print(dataShow)\n",
        "    dataOpen.close()"
      ]
    }
  ]
}