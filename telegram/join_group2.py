# make sure to have telethon and python-dotenv installed
# create a file called .env in the current directory from where you are running the script
# put API_ID and  API_HASH in the .env file in the following format
# VARIABLE=VALUE


from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors.rpcerrorlist import FloodWaitError

from dotenv import load_dotenv
import os
import asyncio

# load_dotenv()
API_ID = ''
API_HASH = ''


CHANNELS = ['TRUSTEDSELLERSHUB3','TRUSTEDSELLERSHUB2','TRUSTEDSELLERSHUB','Hacking_Novaz','nuclearselling','SELLING_FORCE','APSELLERS_14','Escrowers_Gang','United_Nation_Of_Sellers','paytmcricketleagu','pubghacksconfig','Selling1_Drax','SELLING_FORCE','STHBUYSELL','Escrow_Deals','HDSMM_SELLERS','nooblearner29','safe_selling','dmmovies4k_orignal','Infinite_sellers','Naruto_Sellings_2','Naruto_Sellings_3','SELLERS_ARMY','buysellnf','BUY_AND_SELL_DEALS_2','https://t.me/sellingbuyings','CheapPremiumSelling','PunjabiSellers','coctrading','nuclearselling','UNIQUE_SELLERS','APSELLERS_02','wearebrotherss','thefriendsclub','abhishoppiechat','BuySellArena01','Sellers_Adda','APSELLERS_01','AP_SELLERS_14','AP_SELLERS_15','AP_SELLERS_16','sellersgang','APSELLERS_02','APSELLERS_03','APSELLERS_04','APSELLERS_05','inducedseller','PH_CHEATS_DISCUSS','GM_MART','MGMART21334','Selling_kings','PREMUIM_ZONE','Naruto_Sellings','anonselling','narutoselling','peoplessmartstoregroup','SellerBuyerZone','Private_Hulk_Store ','ffchatroom','Flanteredsellers','dbuyingandselling','clasherstrade','SELLING_FORCE_2','Naruto_Sellings_4','newgroup002','SELLING_CITY','selling_hub_one','PREMIUM_SELLING_DEALZ','APSELLERS_06','APSELLERS_07','COC_VS_SELLER','The_Official_Sellers','CrazySellers','accountsellinggrp','flixselling','PREMIUMACCSSELLER','INDIANSELLERS1 ','carder_vegas ','SELLING_FORCE_3','SELLING_BUYING_GROUPS','AnmolShoppingGroup','DONFED_Support','grandleakagegiveawayhall','Sellers_Town','Range_Selling','Sellingbuyingub','LEGEND_OTP_CLUB','TRUSTEDSELLERSHUB4','IndianSellersCrew2','Clashofclans_India_official','Indian_Seller_Group','INDIANSELLERS1','ESCROW_SELLERZ_3','MSBETTINGLUDO','THEHEISTNETWORKGROUP','heistbuyandsell5','Heistbuyandselling','heistbuyandsell','heistbuyandselling4','heistbuyandselling6','Chor_Baazar','Legit_Sellers_xD','APSELLERS_08','United_Nation_Of_Sellers','sellers_panchayat','dealers_nation','Raos_Sellings','APSELLERS_09','APSELLERS_10','sell_buying','HYYGGJK','selerhuvb','Lucifer_Selling_1','SCHOOL_WALI_MASTII','PREMIUM_SELLING_DEALZ_2','SellerzZone','IndianSellersCrew','team_devil_official','instagram_influencer_Group','SHOOTOUT_COMMUNITY_CHATS','opselling','sethselling','sethselling2','ESCROW_ADDA1','selling_hubs','LEGITSELLERSz','buying_sellinggg','SELLERS_TSUNAMI_2','SUPER_SELLERS_3','Supersellers2','SUPER_SELLERS_6','SELLERSUNIVERSE','botpromotion1','gamexpro11','AP_SELLERS_11','AP_SELLERS_012','AP_SELLERS_13','freefireesports7','Wizardkingroyal','gamexpro11','kingsffofficial','buyingandsellingclub','SuperSellerZ','SELLERSxKINGDOM','IndianSellersCrew','Escrow_Addaa','Selling_OP','IndianSellersCrew2','BEST_SELLINGS','JUST_FOR_FUN_GROUP','LordEscrowSelling','ASHUBHAI_CHAT','SELLERSTSUNAMI','MEGA_SELLERS','SELLERS_EMPIRE','powerofsellers','Amazing_sellers_2','FREINDS_CHAT_GROUP','Jodselling','mentalselling','HIDDEN_SELLER_2','HIDDEN_SUPPORTS','SELLINGHIDDEN','SELLINGBUYINGUB','HID_EN_SELL','SUPP_ORT_HI_D_DEN','HIDDEN_DISCUSSION_3','HIDD_EN_SELLER','SELLER_SGANG','HIDDEN_SELLERSS','HIDDEN_SELLERS_1','FREE_FIRE_ID_SELLorBUY','ROBIN_TEACHING','IndianSellers1','IndianSellersCrew3','indianbuyandselling','netflixbuyandselling','otpbuyandselling','IndianSellers3','Sellinghub12288','IndianSellers4','SELLING_CITY','CursedSellers','sellers_here','SELLERS_Z0NE','IndianSellers6','sellingforce3','Sellinghub01','VENOMxSELLERS','VENOMxSELLERS_1','VENOMxSELLERS_2','VENOMxSELLERS_3','VENOMxSELLERS_4','ExtraSellers','ExtraSeller1','ExtraSeller2','ExtraSeller3','ExtraSeller4','ExtraSeller5','ExtraSeller6','ExtraSeller7','ExtraSeller8','ExtraSeller9']
async def main():
    async with TelegramClient('tg_session', API_ID, API_HASH) as client:
        for channel in CHANNELS:
            try:
                await client(JoinChannelRequest(channel))
            except FloodWaitError as fwe:
                print(f'Waiting for {fwe}')
                await asyncio.sleep(delay=fwe.seconds)
            except Exception as err:
                print(f"Encountered an error while joining {channel}\n{err}")

asyncio.run(main())