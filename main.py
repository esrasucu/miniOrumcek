{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPOKqeQvXjnmjj1kbDvsncq",
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
      "execution_count": null,
      "metadata": {
        "id": "75pw_I8U1sPt"
      },
      "outputs": [],
      "source": [
        "import time\n",
        "from dataURL import DataURL\n",
        "from getURL import GetURL\n",
        "\n",
        "useDataURL = DataURL()\n",
        "useGetURL = GetURL()\n",
        "\n",
        "print(\"-:Merhabalar mini örümceğe hoş geldiniz! :-\")\n",
        "print(\"|-----------------------------------------|\")\n",
        "isim = input(\"Lütfen isminizi giriniz: \")\n",
        "print(\"Merhaba!\" '\\n' + isim + '\\n' \"Ben mini örümcek sana nasıl yardımcı olabilirim?\" + \"\\n\")\n",
        "print(\" \")\n",
        "time.sleep(2)\n",
        "\n",
        "while True:\n",
        "    print(\"Lütfen menü numarasını rakam şeklinde giriniz!\")\n",
        "    print(\"MENÜ: '\\n' 0)Çıkış '\\n' 1)URL listele '\\n' 2)URL ekle '\\n' 3)Örümcek gönder '\\n' 4)Sonuçları listele '\\n'\")\n",
        "    print(\"Lütfen menü numarasını rakam şeklinde giriniz!\")\n",
        "    menuSecim = (input(\"Seçiminiz: \"))\n",
        "    if menuSecim.isdigit():\n",
        "        menuSecim = int(menuSecim)\n",
        "        if menuSecim == 0:\n",
        "            print(\"Mini örümcek kapatılıyor...\")\n",
        "            time.sleep(1)\n",
        "            break\n",
        "        elif menuSecim == 1:\n",
        "            useDataURL.dataRead()\n",
        "        elif menuSecim == 2:\n",
        "            useDataURL.dataWrite()\n",
        "        elif menuSecim == 3:\n",
        "            useGetURL.getWeb()\n",
        "        elif menuSecim == 4:\n",
        "            useGetURL.getList()\n",
        "\n",
        "    else:\n",
        "        print(\"Lütfen menü numarasını 0 ile 4 arasında rakam şeklinde giriniz!\")\n",
        "        print(\"Yeniden menüye yönlendiriliyorsunuz.Lütfen bekleyiniz...\")\n",
        "        time.sleep(2)"
      ]
    }
  ]
}