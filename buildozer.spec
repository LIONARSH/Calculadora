name: Build APK

on:
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-22.04

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Setup Java 17
        uses: actions/setup-java@v4
        with:
          distribution: temurin
          java-version: "17"

      - name: Setup Python 3.10
        uses: actions/setup-python@v5
        with:
          python-version: "3.10"

      - name: Setup Android SDK
        uses: android-actions/setup-android@v3

      - name: Accept SDK licenses
        run: yes | sdkmanager --licenses

      - name: Install Android SDK packages
        run: |
          sdkmanager \
            "platform-tools" \
            "platforms;android-33" \
            "build-tools;33.0.2" \
            "cmdline-tools;latest"

      - name: Install Linux dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y \
            zip unzip git \
            autoconf automake libtool \
            pkg-config \
            zlib1g-dev \
            libncurses5-dev \
            libffi-dev \
            libssl-dev \
            libsqlite3-dev \
            libjpeg-dev \
            libpng-dev \
            liblzma-dev \
            build-essential \
            cmake \
            ninja-build

      - name: Install Python packages
        run: |
          python -m pip install --upgrade pip
          pip install Cython==0.29.36
          pip install buildozer

      - name: Cache Buildozer
        uses: actions/cache@v4
        with:
          path: |
            ~/.buildozer
            ~/.gradle
          key: ${{ runner.os }}-buildozer-${{ hashFiles('buildozer.spec') }}

      - name: Clean previous build
        run: |
          rm -rf .buildozer
          rm -rf bin

      - name: Build APK
        run: |
          set -o pipefail
          buildozer -v android debug | tee build.log

      - name: Search APK
        if: always()
        run: |
          find . -name "*.apk"

      - name: Upload APK
        if: success()
        uses: actions/upload-artifact@v4
        with:
          name: Calculadora-APK
          path: |
            bin/*.apk
            **/*.apk
          if-no-files-found: warn

      - name: Upload Build Log
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: build-log
          path: build.log
