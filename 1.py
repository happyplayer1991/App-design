# Implementation of Selenium WebDriver with Python using PyTest

import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.proxy import Proxy, ProxyType
# from seleniumwire import webdriver

# import requests
# import random

# response = requests.get(
#     "https://proxy.webshare.io/api/v2/proxy/list/?mode=direct&page=1&page_size=25",
#     headers={"Authorization": "Token bznh2r2655q5bpz525cohtu6vbugreenvex5hv49"}
# )
# proxy_list = response.json()["results"]
# print(len(proxy_list))
# for proxy in proxy_list:
#     print("{}:{}".format(proxy["proxy_address"], proxy["port"]))

PAIR = "0x77d7acc4f313a338e3745a26ae4f357e6be91d34"
# PAIR = "0x80a0102a1e601c55fd3f136128bb2d222a879ff3"

URL = "https://www.dextools.io/app/en/ether"
DRIVER = "D://work//Aqua//NFT//chromedriver_win32//webdriver.exe"
EXTENSION_PATH = '10.24.2_0.crx'

global chrome_driver
global action


def start():
    while True:
        # i = random.randint(0, len(proxy_list))
        # proxy_url = "{}:{}".format(proxy_list[i]["proxy_address"], proxy_list[i]["port"])
        # print("proxy {} selected - {}".format(i, proxy_url))

        # prox = Proxy()
        # prox.proxy_type = ProxyType.MANUAL
        # prox.http_proxy = proxy_url
        # # prox.socks_proxy = "185.199.229.156:7492"
        # # prox.ssl_proxy = "185.199.229.156:7492"

        # capabilities = webdriver.DesiredCapabilities.CHROME
        # prox.add_to_capabilities(capabilities)
        # chrome_driver= webdriver.Chrome(executable_path=DRIVER, desired_capabilities=capabilities)

        service = DRIVER

        chrome_options = Options()
        chrome_options.add_argument("window-size=1060,400")
        chrome_options.add_extension(EXTENSION_PATH)
        global chrome_driver
        chrome_driver = webdriver.Chrome(
            executable_path=service, chrome_options=chrome_options)

        # options = {
        #     'proxy': {
        #         'http': 'http://stevieg:R0ckstar1@geo.iproyal.com:12321',
        #         'https': 'https://stevieg:R0ckstar1@geo.iproyal.com:12321',
        #     }
        # }

        # global chrome_driver
        # chrome_driver = webdriver.Chrome(executable_path=service,
        #                                  chrome_options=chrome_options,
        #                                  seleniumwire_options=options)

        global action
        action = ActionChains(chrome_driver)

        try:
            new_session()
        except Exception as e:
            print(e)


def new_session():
    # chrome_driver.get("https://ipv4.icanhazip.com")
    # print(chrome_driver.find_element(By.TAG_NAME, "pre").text)
    # sleep(2)

    chrome_driver.get(URL)
    # chrome_driver.maximize_window()
    sleep(2000)

    close_button = WebDriverWait(chrome_driver, timeout=100).until(
        lambda d: d.find_element(By.CLASS_NAME, "close"))
    print("click close button")
    action.move_to_element_with_offset(close_button, 0, 0)
    action.click()
    action.perform()

    # for i in range(3):
    # sleep(2)
    trending_dextools()
    # chrome_driver.refresh()
    # print("{} refreshed".format(i+1))

    chrome_driver.quit()


def trending_dextools():

    # search-contrainer
    search_contrainer = WebDriverWait(chrome_driver, timeout=100).until(
        lambda d: d.find_element(By.CLASS_NAME, "search-container"))
    print("click search container")
    action.move_to_element_with_offset(search_contrainer, 0, 0)
    action.click()
    action.perform()
    sleep(1)

    # pair input
    pair_input = WebDriverWait(chrome_driver, timeout=100).until(
        lambda d: d.find_element(By.CLASS_NAME, "search-pairs"))
    print("input pair")
    pair_input.send_keys(PAIR)
    sleep(1)

    # found pair click
    found_pair = WebDriverWait(chrome_driver, timeout=100).until(
        lambda d: d.find_element(By.CLASS_NAME, "search-result-item"))
    print("found pair")
    action.move_to_element_with_offset(found_pair, 0, 0)
    action.click()
    action.perform()
    sleep(5)

    # # favorit panel close
    # favorit_panel = WebDriverWait(chrome_driver, timeout=100).until(
    #     lambda d: d.find_element(By.TAG_NAME, "app-favorites-list"))
    # print("close favorit panel")
    # close_button = favorit_panel.find_element(By.CLASS_NAME, "close")
    # action.move_to_element_with_offset(close_button, 0, 0)
    # action.click()
    # action.perform()
    # sleep(5)

    try:
        # favorite button
        favorite_button = WebDriverWait(chrome_driver, 100).until(
            EC.presence_of_element_located((By.CLASS_NAME, "favorite-button")))
        print("favorite button click")
        action.move_to_element_with_offset(favorite_button, 0, 0)
        action.click()
        action.perform()
        sleep(1)

        # search token button
        search_token_button = WebDriverWait(chrome_driver, 100).until(
            EC.presence_of_element_located((By.CLASS_NAME, "search-token-button")))
        print("search token button click")
        action.move_to_element_with_offset(search_token_button, 0, 0)
        action.click()
        action.perform()
        sleep(2)

        # close search token panel
        pairs_search_container = WebDriverWait(chrome_driver, 100).until(
            EC.presence_of_element_located((By.CLASS_NAME, "pairs-search-container")))
        close_button = pairs_search_container.find_element(
            By.CLASS_NAME, "close")
        print("close search token panel")
        action.move_to_element_with_offset(close_button, 0, 0)
        action.click()
        action.perform()
        sleep(2)
    except Exception as e:
        print(e)

    try:
        # social container
        social_container = WebDriverWait(chrome_driver, 100).until(
            EC.presence_of_element_located((By.CLASS_NAME, "social-container")))
        print("found social container")
        socials = social_container.find_elements(By.TAG_NAME, "a")
        print(len(socials))

        try:
            # share button click
            action.move_to_element_with_offset(socials[0], 0, 0)
            action.click()
            action.perform()
            sleep(1)

            # share info block
            share_info_block = WebDriverWait(chrome_driver, 100).until(
                EC.presence_of_element_located((By.CLASS_NAME, "share-btn")))
            print("found share info block")
            share_infos = share_info_block.find_elements(By.TAG_NAME, "a")
            # share buttons click
            for share_info in share_infos:
                action.move_to_element_with_offset(share_info, 0, 0)
                action.click()
                action.perform()
                sleep(1)

            # close button click
            share_info_panel = WebDriverWait(chrome_driver, 100).until(
                EC.presence_of_element_located((By.TAG_NAME, "app-social-media-modal")))
            close_button = share_info_panel.find_element(
                By.CLASS_NAME, "close")
            print("close share modal")
            action.move_to_element_with_offset(close_button, 0, 0)
            action.click()
            action.perform()
            sleep(1)
        except Exception as e:
            print(e)

        SOCIALS = ["share", "etherscan", "web", "telegram",
                   "twitter", "coingecko", "???", "????"]
        for i in range(1, len(socials)-2):
            print("{} click".format(SOCIALS[i]))
            action.move_to_element_with_offset(socials[i], 0, 0)
            action.click()
            action.perform()
            chrome_driver.switch_to.window(chrome_driver.window_handles[0])
            sleep(1)

    except Exception as e:
        print(e)

    try:
        # pool-swap tab
        tabs_pool_swap = WebDriverWait(chrome_driver, 100).until(
            EC.presence_of_element_located((By.CLASS_NAME, "tabs-pool-swap")))
        print("found pool-swap tab")
        pool_swap_buttons = tabs_pool_swap.find_elements(By.TAG_NAME, "button")

        # swap tab click
        action.move_to_element_with_offset(pool_swap_buttons[0], 0, 0)
        action.click()
        action.perform()
        sleep(2)

        # low score and low community vote
        try:
            trade_button = chrome_driver.find_element(
                By.CLASS_NAME, "swap-button")
            print("Trade click")
            action.move_to_element_with_offset(trade_button, 0, 0)
            action.click()
            action.perform()
            sleep(2)
        except:
            None

        try:
            claimer_button = chrome_driver.find_element(
                By.CLASS_NAME, "btn-disclaimer")
            print("disclaimer click")
            action.move_to_element_with_offset(claimer_button, 0, 0)
            action.click()
            action.perform()
            sleep(2)
        except:
            None

        # connect wallet click
        connect_wallet_button = WebDriverWait(chrome_driver, 100).until(
            EC.presence_of_element_located((By.CLASS_NAME, "swap-actions")))
        print("connect wallet click")
        action.move_to_element_with_offset(connect_wallet_button, 0, 0)
        action.click()
        action.perform()

        # web3modal provider
        web3_provider = WebDriverWait(chrome_driver, 100).until(
            EC.presence_of_element_located((By.CLASS_NAME, "web3modal-provider-wrapper")))
        print("web3modal provider click")
        action.move_to_element_with_offset(web3_provider, 0, 0)
        action.click()
        action.perform()
        sleep(1)

        web3_provider_close = WebDriverWait(chrome_driver, 100).until(
            EC.presence_of_element_located((By.CLASS_NAME, "walletconnect-modal__close__wrapper")))
        print("web3modal close click")
        action.move_to_element_with_offset(web3_provider_close, 0, 0)
        action.click()
        action.perform()
        sleep(2)
    except Exception as e:
        print(e)

    sleep(2)


start()
