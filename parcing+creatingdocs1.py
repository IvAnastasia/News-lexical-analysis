pip install requests
pip install beautifulsoup4

import requests
import re
from bs4 import BeautifulSoup


def parse(link):
    if 'meduza.' in link:
        return meduza(link)
    if 'novayagazeta' in link:
        return '***the place for your manually NOVAYA GAZETA got text***' #надо дополнить текст вручную
    if 'tvrain' in link:
        return rain(link)
    if 'rbc' in link:
        return rbc(link)
    if 'tsargrad.tv' in link:
        return tsar(link)
    if 'ria.' in link:
        return ria(link)
    if 'russian.rt' in link:
        return rt(link)
    if 'rg.ru' in link:
        return rg(link)


def meduza(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.text, "html.parser")
    alltext = soup.findAll('p')
    newstext = soup.title.text + '. '
    for data in alltext:
        newstext = newstext + data.text + ' '
    newstext = newstext.replace(' — Meduza', '')
    newstext = newstext.replace(
        'Данное сообщение (материал) создано и (или) распространено иностранным средством массовой информации, выполняющим функции иностранного агента, и (или) российским юридическим лицом, выполняющим функции иностранного агента.  ',
        '')
    newstext = newstext.replace(
        'Данное сообщение (материал) создано и (или) распространено иностранным средством массовой информации, выполняющим функции иностранного агента, и (или) российским юридическим лицом, выполняющим функции иностранного агента.  ',
        '')
    return newstext + '\n'

def rain(link):
    reg = re.compile(r"Вы уже подписчик[\s*\S*]*")
    page = requests.get(link)
    soup = BeautifulSoup(page.text, "html.parser")
    alltext = soup.findAll('p')
    newstext = soup.title.text + '. '
    for data in alltext:
        newstext = newstext + data.text + ' '
    newstext = re.sub(reg, '', newstext)
    return newstext + '\n'


def rbc(link):
    reg1 = re.compile(r" :: .+ :: РБК")
    reg2 = re.compile(r"Видео[\s*\S*]*")
    reg3 = re.compile(r"Фото на превью:.*")
    reg4 = re.compile(r"\s+Video")
    page = requests.get(link)
    soup = BeautifulSoup(page.text, "html.parser")
    alltext = soup.findAll('p')
    newstext = soup.title.text + '. '
    for data in alltext:
        if data.find(class_='article__inline-item__title') is not None:
            pass
        else:
            newstext = newstext + data.text + ' '
    newstext = re.sub(reg1, '', newstext)
    newstext = re.sub(reg2, '', newstext)
    newstext = re.sub(reg3, '', newstext)
    newstext = re.sub(reg4, '', newstext)
    return newstext + '\n'


def tsar(link):
    reg1 = re.compile(r"\s{1,}Средство массовой информации сетевое издание[\s*\S*]*")
    reg2 = re.compile(r"Уважаемые читатели «Царьграда»![\s*\S*]*")
    page = requests.get(link)
    soup = BeautifulSoup(page.text, "html.parser")
    alltext = soup.findAll('p')
    newstext = soup.title.text + '. '
    for data in alltext:
        newstext = newstext + data.text + ' '
    newstext = re.sub(reg1, '', newstext)
    newstext = re.sub(reg2, '', newstext)
    return newstext + '\n'


def ria(link):
    reg1 = re.compile(r'''<div itemprop="headline">(.+)<\/div><div itemprop="name">''')
    reg2 = re.compile(r'''<div itemprop="articleBody">(.+)\.<\/div>''')
    reg3 = re.compile(r".+(( РИА Новости)|( Радио Sputnik.))")
    reg4 = re.compile(r"<.+>")
    page = requests.get(link)
    soup = page.text
    head = ''
    body = ''
    if re.findall(reg1, soup):
        head = re.findall(reg1, soup)[0]
    if re.findall(reg2, soup):
        body = re.findall(reg2, soup)[0]
        body = re.sub(reg3, '', body)
    else:
        soup = BeautifulSoup(page.text, "html.parser")
        alltext = soup.findAll('p')
        for data in alltext:
            body = body + data.text
    body = re.sub(reg3, '', body)
    newstext = head + '.' + body
    newstext = re.sub(reg3, '', newstext)
    newstext = re.sub(reg4, '', newstext)
    return newstext + '\n'

def rt(link):
    reg1 = re.compile(r"© Автономная некоммерческая организация.*")
    reg2 = re.compile(r"<.+>")
    page = requests.get(link)
    soup = BeautifulSoup(page.text, "html.parser")
    alltext = soup.findAll('p')
    newstext = soup.title.text + '. '
    for data in alltext:
        newstext = newstext + data.text + ' '
    newstext = newstext.replace(' — РТ на русском', '')
    newstext = re.sub(reg1, '', newstext)
    newstext = re.sub(reg2, '', newstext)
    return newstext + '\n'


def rg(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.text, "html.parser")
    alltext = soup.findAll('p')
    newstext = soup.title.text + '. '
    newstext = newstext.replace(' — Российская газета', '')
    for data in alltext:
        newstext = newstext + data.text
    return newstext + '\n'


rus_links = [['https://tsargrad.tv/news/novyj-gornyj-kurort-v-sochi-obojdetsja-v-80-mlrd-rublej_342302',
              'https://ria.ru/20210408/investitsii-1727348071.html'],
             [
                 'https://tsargrad.tv/news/ne-dozhil-nemnogo-do-100-let-v-velikobritanii-skonchalsja-muzh-korolevy-elizavety-ii_342576',
                 'https://ria.ru/20210409/filipp-1727580052.html',
                 'https://russian.rt.com/world/news/851137-suprug-elizavety-ii-filipp',
                 'https://rg.ru/2021/04/09/skonchalsia-muzh-korolevy-velikobritanii-elizavety-ii.html'],
             ['https://tsargrad.tv/news/advokat-jeks-policejskogo-zaharchenko-zaderzhan-za-krupnuju-vzjatku_342618',
              'https://ria.ru/20181002/1529842408.html',
              'https://rg.ru/2021/04/09/sledstvie-prosit-arestovat-advokata-eks-polkovnika-zaharchenko.html'],
             ['https://tsargrad.tv/news/amerikanskij-korabl-crew-dragon-pristykovalsja-k-mks-nasa_348375',
              'https://ria.ru/20210424/kosmos-1729755075.html',
              'https://russian.rt.com/science/news/856210-korabl-crew-dragon',
              'https://rg.ru/2021/04/23/korabl-crew-dragon-s-chetyrmia-astronavtami-na-bortu-startoval-k-mks.html'],
             [
                 'https://tsargrad.tv/news/ischeznuvshaja-podlodka-najdena-u-beregov-bali-v-podvodnom-plenu-byli-53-cheloveka_348372',
                 'https://ria.ru/20210424/podlodka-1729758030.html',
                 'https://russian.rt.com/world/news/856207-podlodka-indoneziya-obnaruzhenie',
                 'https://rg.ru/2021/04/24/propavshuiu-indonezijskuiu-podlodku-nashli-na-glubine-850-metrov.html'],
             ['https://tsargrad.tv/news/janukovich-aksjonov-poklonskaja-zelenskij-vvjol-sankcii-protiv-27-lic_342750',
              'https://ria.ru/20210409/sanktsii-1727632194.html',
              'https://russian.rt.com/ussr/news/851336-zelenskiy-sankzii-ukraina'],
             ['https://radiosputnik.ria.ru/20210409/osetiya-1727569275.html',
              'https://russian.rt.com/russia/news/851173-putin-predlozhil-menyailo-post',
              'https://rg.ru/2021/04/09/reg-skfo/putin-naznachil-meniajlo-vrio-glavy-severnoj-osetii.html'],
             [
                 'https://tsargrad.tv/news/na-fone-provala-zapadnyh-preparatov-v-rossii-ne-bylo-ni-odnoj-smerti-posle-vakcinacii_342582',
                 'https://ria.ru/20210409/koronavirus-1727536106.html',
                 'https://russian.rt.com/russia/news/851125-roszdravnadzor-vakcina-koronavirus',
                 'https://rg.ru/2021/04/09/roszdravnadzor-otvetil-na-soobshcheniia-smi-o-smerti-pacientov-posle-vakcinacii.html'],
             [
                 'https://tsargrad.tv/news/poplatilis-s-tik-tok-vzyskali-25-mln-rublej-za-otkaz-udaljat-prizyvy-na-miting-v-moskve_341275',
                 'https://radiosputnik.ria.ru/20210406/tiktok-1727051537.html',
                 'https://russian.rt.com/russia/news/849966-tiktok-shtraf-akcii',
                 'https://rg.ru/2021/04/06/sud-oshtrafoval-tiktok-na-26-mln-rublej.html'],
             [
                 'https://tsargrad.tv/news/pozval-putina-na-vstrechu-i-zakolebalsja-zelenskomu-otsovetovali-ehat-v-stolicu-agressora_348312',
                 'https://radiosputnik.ria.ru/20210424/1729745747.html',
                 'https://russian.rt.com/world/news/856153-putin-zelenskii-vstrecha'],
             [
                 'https://tsargrad.tv/news/bomba-lavrova-srabotala-v-kremle-putin-postavil-nedrugov-rossii-pered-faktom_348381',
                 'https://ria.ru/20210423/ukaz-1729717086.html',
                 'https://russian.rt.com/world/news/856103-putin-ukaz-protivodeistvie-strany',
                 'https://rg.ru/2021/04/23/putin-utverdil-mery-vozdejstviia-na-nedruzhestvennye-gosudarstva.html'],
             ['https://radiosputnik.ria.ru/20210423/sanktsii-1729698868.html',
              'https://russian.rt.com/ussr/news/856028-belorussiya-zapret-vvoz-tovary'],
             [
                 'https://tsargrad.tv/news/vot-pribaltika-vyjozhivalas-voennyj-jekspert-nameknul-na-radikalnyj-otvet-chehii_347505',
                 'https://ria.ru/20210424/pivo-1729754181.html',
                 'https://russian.rt.com/world/news/856213-chehiya-import-tovarov',
                 'https://rg.ru/2021/04/24/rossiia-mozhet-ogranichit-import-cheshskogo-piva.html'],
             ['https://spb.tsargrad.tv/news/izrail-nachal-masshtabnuju-ataku-na-sektor-gaza_354809',
              'https://ria.ru/20210514/izrail-1732308768.html',
              'https://russian.rt.com/world/news/861846-izrail-rakety-sektor-gaza',
              'https://rg.ru/2021/05/14/armiia-izrailia-obiavila-o-nachale-nazemnoj-i-vozdushnoj-ataki-sektora-gaza.html'],
             [
                 'https://spb.tsargrad.tv/news/zaderzhanie-jeks-zampreda-pravitelstva-mordovii-v-ajeroportu-popalo-na-video_354892',
                 'https://ria.ru/20210514/vzyatka-1732246553.html',
                 'https://russian.rt.com/russia/news/861853-sk-zaderzhanie-mordoviya',
                 'https://rg.ru/2021/05/14/reg-pfo/byvshij-vice-premer-pravitelstva-mordovii-zaderzhan-po-podozreniiu-v-korrupcii.html'],
             [
                 'https://spb.tsargrad.tv/news/maksimalnoe-nakazanie-gosobvinenija-poprosilo-14-let-tjurmy-dlja-rukovodstva-tc-zimnjaja-vishnja_354118',
                 'https://ria.ru/20210512/sroki-1731965536.html',
                 'https://rg.ru/2021/05/12/reg-sibfo/obvinenie-poprosilo-ot-5-do-145-let-dlia-figurantov-dela-zimnej-vishni.html']]

indep_links = [[
                   'https://meduza.io/news/2021/04/08/v-sochi-planiruyut-postroit-novyy-gornyy-kurort-dolina-vasta-v-proekt-vlozhat-80-milliardov-rubley',
                   'https://www.rbc.ru/business/08/04/2021/606eca419a79470ab4e685b9'],
               ['https://meduza.io/news/2021/04/09/umer-suprug-korolevy-elizavety-ii-gertsog-edinburgskiy',
                'https://novayagazeta.ru/articles/2021/04/09/skonchalsia-suprug-korolevy-velikobritanii-prints-filipp-emu-bylo-99-let',
                'https://tvrain.ru/news/umer_muzh_britanskoj_korolevy_prints_filipp-527900',
                'https://www.rbc.ru/politics/09/04/2021/6070348b9a79470f371900c5?from=from_main_1'],
               [
                   'https://novayagazeta.ru/articles/2021/04/09/advokata-eks-polkovnika-zakharchenko-arestovali-po-delu-o-posrednichestve-pri-poluchenii-vziatki',
                   'https://tvrain.ru/news/advokata_byvshego_polkovnika_mvd_dmitrija_zaharchenko_arestovali_po_delu_o_vzjatke-527933/',
                   'https://www.rbc.ru/society/09/04/2021/607087459a794734833c0cab?from=newsfeed'],
               ['https://www.rbc.ru/society/09/04/2021/607087459a794734833c0cab?from=newsfeed',
                'https://novayagazeta.ru/articles/2021/04/24/korabl-crew-dragon-2-kompanii-spacex-uspeshno-sostykovalsia-s-mks',
                'https://tvrain.ru/news/kosmicheskij_korabl_crew_dragon_uspeshno_sostykovalsja_s_mks-519443/',
                'https://www.rbc.ru/rbcfreenews/6083e5d49a7947617211bb0c?from=newsfeed'],
               [
                   'https://meduza.io/news/2021/04/24/propavshaya-u-beregov-indonezii-podlodka-zatonula-na-bortu-nahodilis-53-cheloveka',
                   'https://www.rbc.ru/society/24/04/2021/6083dc1b9a79475ea0b3d213?from=from_main_3'],
               ['https://www.rbc.ru/politics/09/04/2021/60709dfe9a79473966c5000b'],
               [
                   'https://meduza.io/news/2021/04/09/putin-smenil-glavu-severnoy-osetii-novym-rukovoditelem-regiona-stal-postpred-v-sibiri-sergey-menyaylo',
                   'https://novayagazeta.ru/articles/2021/04/09/putin-podpisal-ukaz-ob-otstavke-bitarova-s-posta-glavy-severnoi-osetii',
                   'https://tvrain.ru/news/putin_smenil_glavu_severnoj_osetii-527902/',
                   'https://nsk.rbc.ru/nsk/09/04/2021/60704c399a79471dad961ee0'],
               [
                   'https://meduza.io/feature/2021/04/09/euobserver-u-10-chelovek-v-rossii-byli-oslozhneniya-posle-vaktsinatsii-sputnikom-v-chetvero-iz-nih-umerli',
                   'https://tvrain.ru/news/roszdravnadzor_zajavil_ob_otsutstvii_smertej_iz_za_primenenija_rossijskih_vaktsin_ot_covid_19-527899/',
                   'https://www.rbc.ru/society/09/04/2021/606ffb169a7947719c820b12'],
               [
                   'https://novayagazeta.ru/articles/2021/04/06/sud-v-moskve-oshtrafoval-tiktok-na-25-mln-rublei-za-otkaz-udalit-prizyvy-k-podrostkam-vyiti-na-protesty',
                   'https://tvrain.ru/news/sud_oshtrafoval_tiktok_na_25_milliona_rublej_za_neudalenie_prizyvov_k_protestam-527674/',
                   'https://www.rbc.ru/society/06/04/2021/606c46129a794743d611542f'],
               [
                   'https://novayagazeta.ru/articles/2021/04/24/strannoe-predlozhenie-kiev-nazval-nevozmozhnoi-vstrechu-putina-i-zelenskogo-v-moskve',
                   'https://tvrain.ru/news/v_kieve_nazvali_nevozmozhnoj_vstrechu_zelenskogo_i_putina_v_moskve-528812/',
                   'https://www.rbc.ru/politics/24/04/2021/60839be49a79474ffa97835c'],
               [
                   'https://meduza.io/news/2021/04/23/putin-ogranichil-dipmissii-nedruzhestvennyh-gosudarstv-v-vozmozhnosti-nanimat-sotrudnikov-iz-rossii',
                   'https://novayagazeta.ru/articles/2021/04/23/putin-podpisal-ukaz-o-deistviiakh-v-otvet-na-nedruzhestvennye-deistviia-inostrannykh-gosudarstv',
                   'https://www.rbc.ru/politics/23/04/2021/608313a29a7947347fa80dd0'],
               [
                   'https://meduza.io/news/2021/04/23/v-belarus-zapretili-vvozit-mashiny-skoda-avtomasla-liqui-moly-i-kosmetiku-nivea-posle-otkaza-etih-brendov-sponsirovat-chm-po-hokkeyu-v-minske',
                   'https://novayagazeta.ru/articles/2021/04/23/vlasti-belarusi-zapretili-vvozit-v-stranu-produktsiiu-skoda-auto-liqui-moly-i-beiersdorf-eti-kompanii-partnery-chm-po-khokkeiu',
                   'https://www.rbc.ru/rbcfreenews/6082e2859a7947252cf48cd8'],
               [
                   'https://meduza.io/news/2021/04/24/v-otvet-na-vysylku-diplomatov-rossiya-planiruet-ogranichit-import-cheshskogo-piva',
                   'https://tvrain.ru/news/kommersant_vlasti_rossii_zadumalis_ob_ogranichenii_importa_cheshskogo_piva-528814/',
                   'https://www.rbc.ru/politics/24/04/2021/6083b21d9a794754851c785a'],
               [
                   'https://meduza.io/news/2021/05/14/izrail-provel-krupneyshiy-s-nachala-konflikta-obstrel-gazy-za-40-minut-samolety-obstrelyali-150-tseley-ataku-podderzhivali-artilleriyskim-ognem',
                   'https://novayagazeta.ru/articles/2021/05/13/armiia-izrailia-nachala-nastupatelnuiu-nazemnuiu-operatsiiu-v-sektore-gaza',
                   'https://tvrain.ru/news/izrail_nachal_vozdushnuju_i_nazemnuju_ataku_sektora_gaza-529937/',
                   'https://www.rbc.ru/politics/14/05/2021/609d9add9a7947b0904398fc'],
               [
                   'https://meduza.io/news/2021/05/14/syna-byvshego-glavy-mordovii-zaderzhali-po-podozreniyu-v-dache-vzyatki',
                   'https://novayagazeta.ru/articles/2021/05/13/v-sheremetevo-zaderzhali-syna-byvshego-glavy-mordovii-merkushkina',
                   'https://tvrain.ru/news/v_sheremetevo_zaderzhan_byvshij_vitse_gubernator_mordovii_aleksej_merkushkin-529921/',
                   'https://www.rbc.ru/politics/13/05/2021/609d70ef9a7947a3d8c2c9e8'],
               [
                   'https://meduza.io/news/2021/05/12/prokuratura-zaprosila-ot-pyati-do-14-5-let-kolonii-dlya-figurantov-dela-o-pozhare-v-zimney-vishne',
                   'https://novayagazeta.ru/articles/2021/05/12/gosobvinenie-zaprosilo-do-145-goda-lisheniia-svobody-figurantam-dela-o-pozhare-v-zimnei-vishne',
                   'https://tvrain.ru/news/prokuror_zaprosil_ot_5_do_145_let_kolonii_dlja_figurantov_dela_o_pozhare_v_zimnej_vishne-529809/',
                   'https://www.rbc.ru/society/12/05/2021/609bc26d9a7947148deba741']]
n = 1
for li in indep_links:
    with open('indepnew' + str(n) + '.txt', 'a', encoding='utf-8') as file:
        for link in li:
            newstext = parse(link)
            if type(newstext) != None:
                file.write(newstext)
    n += 1

n = 1
for li in rus_links:
    with open('rusnew' + str(n) + '.txt', 'a', encoding = 'utf-8') as file:
        for link in li:
            newstext = parse(link)
            if type(newstext) != None:
                file.write(newstext)
    n += 1

#check these files and start "creatingdocs2" code
