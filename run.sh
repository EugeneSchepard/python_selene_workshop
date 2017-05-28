#!/bin/bash
rm -rf report

mkdir -p report

rm -rf allure-report

pytest tests --alluredir=report

allure_gen/bin/allure generate report