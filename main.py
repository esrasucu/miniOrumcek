{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNa9v9vvV/LHZyAmFBb0deM",
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
        "<a href=\"https://colab.research.google.com/github/esrasucu/miniOrumcek/blob/main/main.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import time\n",
        "from dataURL import DataURL\n",
        "from getURL import GetURL\n",
        "\n",
        "useDataURL = DataURL()\n",
        "useGetURL = GetURL()\n",
        "\n",
        "print(\"-: Merhaba mini örümceğe hoş geldiniz!:-\")\n",
        "print(\"|------------------------------|\")\n",
        "print(\"\")\n",
        "time.sleep(2)\n",
        "\n",
        "while true:\n",
        "  print(\"menü:0)Çıkış 1)URL Listele2)URL Ekle 3)Örümcek gönder 4)Sonuçları Listele 5\")\n",
        "  menuSecim = int( input(\"Tercihiniz:\"))\n",
        "  if menuSecim == 0:\n",
        "    print(\"Mini örümcek kapatılıyor...\")\n",
        "    time.sleep(1)\n",
        "    break\n",
        "elif menuSecim == 1:\n",
        "  useDataURL.dataRead()\n",
        "elif menuSecim == 2:\n",
        "  useDataURL.dataWrite()\n",
        "elif menuSecim == 3:\n",
        "  useGetURL.getWeb()\n",
        "elif menuSecim == 4:\n",
        "  useGetURL.getList()\n",
        "\n",
        "else:\n",
        "  print(\"Lütfen menü numarasına 0 ile 4 arası rakam giriniz.\")\n",
        "  print(\"Yeniden menüye yönlendiriliyorsunuz bekleyin!...\")\n",
        "  time.sleep(2)\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 106
        },
        "collapsed": true,
        "id": "iEthM8rExOrg",
        "outputId": "8d036d90-6a1f-4508-d376-8f60aa222399"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "error",
          "ename": "SyntaxError",
          "evalue": "invalid syntax (<ipython-input-5-1767d6ba8bdc>, line 20)",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-5-1767d6ba8bdc>\"\u001b[0;36m, line \u001b[0;32m20\u001b[0m\n\u001b[0;31m    elif menuSecim == 1:\u001b[0m\n\u001b[0m    ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
          ]
        }
      ]
    }
  ]
}