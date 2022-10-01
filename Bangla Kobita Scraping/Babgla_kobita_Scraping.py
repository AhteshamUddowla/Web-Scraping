!pip install requests-html

from requests_html import HTMLSession
session = HTMLSession()

def bangla_kobita_scrapping(url, author, kobita):
  updated_url = url + author + "/" + kobita + "/"
  print(updated_url) 
  r = session.get(updated_url)
  author_pattern = "body > div.container > div.row.body-content > div.col-md-8 > div:nth-child(5) > div.author-name > a > span"
  #print(r.html.find(author_pattern)[0].text)
  poem_name_pattern = "body > div.container > div.row.body-content > div.col-md-8 > div:nth-child(5) > h1 > span"
  #print(r.html.find(poem_name_pattern)[0].text)
  kobita_des_pattern = "body > div.container > div.row.body-content > div.col-md-8 > div:nth-child(5) > div.post-content.noselect"
  #print(r.html.find(kobita_des_pattern)[0].text)
  poem_viewed_catagory_pattern = "body > div.container > div.row.body-content > div.col-md-8 > div:nth-child(5) > div.post-summary"
  #print(r.html.find(poem_viewed_catagory_pattern)[0].text)

  author_name = [i.text for i in r.html.find(author_pattern)]
  poem_name = [i.text for i in r.html.find(poem_name_pattern)]
  kobita_des = [i.text for i in r.html.find(kobita_des_pattern)]
  poem_viewed_catagory = [i.text for i in r.html.find(poem_viewed_catagory_pattern)]
  
  with open(f"{author}/{poem_name[0]}", "w") as f:
    f.write("Poem Name, Author, Poem Description, Poem Viewed & Catagory\n")
    for poem_name, author, poem_des, poem_view_catagory in zip(poem_name, author_name,  kobita_des, poem_viewed_catagory):
      f.write(f"{poem_name},\n{author},\n\n{poem_des},\n\n{poem_view_catagory}")
      f.write("\n")

url = "https://www.bangla-kobita.com/"
dic = {"sufiakamal":["aziker-shishu", "azoo-dake", "basonti", "hae-mohan-neta", "hemonto", "itol-bitol", "jonmechi-ei-deshe", "kaler-jatrrar-dhonee", "kaljoyee", "mithathe-jothor-khuda", "nari-o-dhoritree", "polli-smrity", "poth-nohe-antohin", "prarthona", "remember", "sajher-maya", "sleep", "tadere-shoron-kori", "tomar-se-prem"], 
       "jasimuddin":["nokshi-kathar-maath-1", "nokshi-kathar-maath-2", "nokshi-kathar-maath-3","nokshi-kathar-maath-4","nokshi-kathar-maath-5", "nokshi-kathar-maath-6", "nokshi-kathar-maath-7", "nokshi-kathar-maath-8", "nokshi-kathar-maath-9", "nokshi-kathar-maath-10", "nokshi-kathar-maath-11", "nokshi-kathar-maath-12", "nokshi-kathar-maath-13", 
                     "nokshi-kathar-maath-14", "nimontron", "paler-nao", "eto-hashi-kothay-pele", "mamarbadi", "post20160508085944", "post20160508090532", "post20160508091251", "post20160508091423", "post20160508123603", "post20160508124404", "post20160508124806", "post20160508010531", "post20160508011119", "post20160508011736", "post20160508012254", 
                     "post20160508012424","post20160508012653", "post20160508013749", "post20160508020640", "post20160508021236", "post20160508021604", "post20160508021902", "post20160508022235", "post20160509054522", "post20160509054757", "post20160509055044", "post20160509055245", "post20160509055404", "post20160509055528", "post20160509055953", 
                     "post20160509060128", "post20160509060307", "post20160509060450", "post20160509060811", "post20160510090204", "post20160510012032"],
       "nazrulislam":["amader-nari", "nazrul-lichu-chor", "jagoroni", "mohorrom", "korbani", "umar-faruk", "hindu-muslim-shomporko", "daridro", "mora-jhonjhar-moto-uddam", "komolpasa", "kheaparertorony", "dhumketu", "roctoshorodhony", "post20150307032729", "kuhelika", "ganeraral", "tomayporechemone", "pothochary", "borshabiday", "batayon", "hindumuslimjuddho", 
                      "ashuproyangity", "jagoron", "jhorogan", "dusassonerroktopan", "purnoovinondon", "milongan", "mohantermoh", "lavandish", "sohidieid", "superbondona", "shammobadi", "falgun", "bidayshorone", "sahebomemsaheb", "krishokereid", "bagichabulbuly", "cholcholchol", "bodhu-mitilona-sadh", "modir-swopone-momo-mon-voboney-jaago", "aji-money-money-lagey-hori", 
                      "goviir-nishithey-ghum-vengey-jai", "jare-hat-diye-mala-ditey-paroni", "harano-hiar-nikunjo-pothey", "shunno-e-bukey-pakhi-mor-ai", "mago-chinmoi-dhorey-ai", "momtaj-momtaj", "jonom-jonom-gelo", "voria-poran-shunitesi-gan", "ogo-prio-tobo-gaan"],
       "jibanananda":["at-bochor-age-ekdin", "boner-chatok-moner-chatok", "neelima", "ami-kobi-shei-kobi", "banglar-mukh", "smriti", "ostochande", "hridoye-premer-din", "she", "bediya", "ghora", "nabik", "bodh", "taratiri-kotha-hoy", "niralok", "sthobir-joubon", "nabiki", "shovab", "diptii", "shomorurh", "pakhira", "loken-boser-journal", "ekti-nokkhatra-ashe", "shurjotamshi",
                      "shokun", "amake-ekti-kotha-dao", "shawpno", "shob", "shohor", "firey-esho", "shit-raat", "hai-pakhi-ekdin-kaliidohe-chilo-ki-na", "shonar-khachar-buke-rohibo-na-aami", "sandhya-hoi", "shoshaner-deshe-tumi-ashiaso", "jedin-shoria-jabo-tomar-kas-theke", "je-shaliks-morey-jai-kuashai", "joto-din-beche-aasi", "jokhon-mrittur-ghumey-shue-robo",
                      "manusher-betha-aami-paye-gesi", "monye-hoy-ekdin-akasher", "vebe-vebe-betha-pabo", "vijey-hoye-ashe-meghe-e-dupur", "batashe-dhaner-shobdo-shuniasi", "prithibi-royese-byasto", "prithibir-pothey-aami-bohudin-bash-korey", "dur-prithibir-gondhey-vore-othey", "tumi-kano-bohu-durey", "charidikey-shantir-bati", "tobu-taha-vul-jaani"],
       "rabindranath":["bojhapora", "jhorer-din-e", "shuptotthita", "nidrita", "koto-ojanare-janaile-tumi", "har-mana-haar-porabo-tomar-gole", "jedin-futlo-komol-kichui-jani-nai", "sha-jahan", "aral-diye-lukiye-gele", "jhulon", "chitto-tomay-nityo-hobe", "amar-e-prem", "akashtole-uthlo-fute", "khonika", "jabar-din", "daymochon", "prarthona", "neydondo", "hing-ting-chhot", "niruddesh-jatra", 
                       "durbhaga-desh", "puroshkar", "ore-nobin-ore-amar-kacha", "borshar-din-e", "gaaner-pare", "megher-pore-megh-jomechhe", "byertho", "chhol", "krishnokoli", "manoshee", "dui-bigha-jomi", "puraton-bhritto", "ami-bohu-bashonai-pranpone-chai", "bishorjon", "chiro-ami", "amar-poth-chaowatei-ananda", "chhoy", "okkhomota", "okkhoma", "onger-badhone-badhapora-amar-pran", "ochol-smriti",
                       "ochola-buri", "shobhyotar-proti", "lajmoyi", "shopnoruddho", "rajbichar", "sporshomoni", "arshi", "ontorjami", "akasher-chad"]
       }
       
for author in dic:
  for kobita in dic[author]:
    bangla_kobita_scrapping(url, author, kobita)
