{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOL4h+bZ1MrtU4tAOjF+wcF",
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
        "<a href=\"https://colab.research.google.com/github/esrasucu/miniOrumcek/blob/main/getURL.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "S2tkXWpk5I5p"
      },
      "outputs": [],
      "source": [
        "import os\n",
        "import time\n",
        "import urllib.request\n",
        "from bs4 import BeautifulSoup\n",
        "class GetURL:\n",
        "\n",
        "\n",
        "    dataFile = \"dataURL.txt\"\n",
        "    getFile = \"getURL.txt\"\n",
        "\n",
        "    def __init__(self):\n",
        "        fileTest = open(self.getFile, \"a\")\n",
        "        fileTest.close()\n",
        "\n",
        "    def getWeb(self):\n",
        "\n",
        "        print(\"Örümcek çalışıyor...\")\n",
        "\n",
        "        dataOpen = open(self.dataFile, \"r\")\n",
        "        getOpen = open(self.getFile, \"w\")\n",
        "\n",
        "        for dataGet in dataOpen:\n",
        "            webSite = urllib.request.urlopen(dataGet)\n",
        "            getBytes = webSite.read()\n",
        "            webPage = getBytes.decode(\"utf8\")\n",
        "            webSite.close()\n",
        "            soup = BeautifulSoup(webPage, 'html.parser')\n",
        "            getOpen.write(dataGet.strip() + \" - \" + soup.title.contents[0] + \"\\n\")\n",
        "            print(dataGet)\n",
        "        dataOpen.close()\n",
        "        getOpen.close()\n",
        "\n",
        "        print(\"Çalışma tamamlandı!\")\n",
        "\n",
        "    def getList(self):\n",
        "        getOpen = open(self. getFile, \"r\")\n",
        "        if os.stat(self.getFile).st_size == 0:\n",
        "            print(\"Üzgünüm, henüz ziyaret edilmiş adres yok.\")\n",
        "        else:\n",
        "            print(\"Ziyaret edilmiş adresler var...\")\n",
        "            print(\"Lütfen bekleyiniz!\")\n",
        "            time.sleep(1)\n",
        "        for dataShow in getOpen:\n",
        "            print(dataShow)\n",
        "        getOpen.close()"
      ]
    }
  ]
}