from otree.api import *
import random


doc = """
Your app description
"""
#from iomotions.otree.pages import ScenePage

'''class QuizPage(ScenePage):
    scene_name = 'WordList' '''

class C(BaseConstants):
    NAME_IN_URL = 'Wordlist'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    #OPTIONS = ['analysis','approach','area','assessment','assume','authority','available','benefit','concept','consistent','constitutional','context','contract','create','data','definition','derived','distribution','economic','environment','established','estimate','evidence','export','factors','financial','formula','function','identified','income','indicate','individual','interpretation','involved','issues','labour','legal','legislation','major','method','occur','percent','period','policy','principle ','procedure','process','required','research','response','role','section','sector','significant','similar','source','specific','structure','theory','variables ','achieve','acquisition','administration','affect','appropriate','aspects','assistance','categories','chapter','commission','community','complex','computer','conclusion','conduct','consequences','construction','consumer','credit','cultural','design','distinction','elements','equation','evaluation','features','final','focus','impact','injury','institute','investment','items','journal','maintenance','normal','obtained','participation','perceived','positive','potential','previous','primary','purchase','range ','region','regulations','relevant','resident','resources','restricted','security','sought','select','site','strategies','survey','text','traditional','transfer','alternative','circumstances','comments','compensation','components','consent','considerable','constant','constraints','contribution','convention','coordination','core','corporate','corresponding','criteria','deduction','demonstrate','document','dominant','emphasis','ensure','excluded','framework','funds','illustrated','immigration','implies','initial','instance','interaction','justification','layer','link','location','maximum','minorities','negative','outcomes','partnership','philosophy','physical','proportion','published','reaction','registered','reliance','removed','scheme','sequence','sex','shift','specified','sufficient','task','technical','techniques','technology','validity','volume','access','adequate','annual','apparent','approximated','attitudes','attributed','civil','code','commitment','communication','concentration','conference','contrast','cycle','debate','despite','dimensions','domestic','emerged','error','ethnic','goals','granted','hence','hypothesis','implementation','implications','imposed','integration','internal','investigation','job','label','mechanism','obvious','occupational','option','output','overall','parallel','parameters','phase','predicted','principal','prior','professional','project','promote','regime','resolution','retained','series','statistics','status','stress','subsequent','sum','summary','undertaken','academic','adjustment','alter','amendment','aware','capacity','challenge','clause','compounds','conflict','consultation','contact','decline','discretion','draft','enable','energy','enforcement','entities','equivalent','evolution','expansion','exposure','external','facilitate','fundamental','generated','generation','image','liberal','licence','logic','marginal','medical','mental','modified','monitoring','network','notion','objective','orientation','perspective','precise','prime','psychology ','pursue','ratio','rejected','revenue','stability','styles','substitution','sustainable','symbolic','target','transition','trend','version','welfare','whereas ','abstract','accurate','acknowledged','aggregate','allocation','assigned','attached','author','bond','brief','capable','cited','cooperative','discrimination','display','diversity','domain','edition','enhanced','estate','exceed','expert','explicit','federal','fees','flexibility','furthermore','gender','ignored','incentive','incidence','incorporated','index','inhibition','initiatives','input','instructions','intelligence','interval','lecture','migration','minimum','ministry','motivation','neutral ','nevertheless','overseas','preceding','presumption','rational','recovery','revealed','scope','subsidiary','tapes','trace','transformation','transport','underlying','utility ','adaptation','adults','advocate','aid','channel','chemical','classical','comprehensive','comprise','confirmed','contrary','converted','couple','decades','definite','deny','differentiation','disposal','dynamic','eliminate','empirical','equipment','extract','file','finite','foundation','global','grade','guarantee','hierarchical','identical','ideology','inferred','innovation','insert','intervention','isolated','media','mode','paradigm','phenomenon','priority','prohibited','publication ','quotation','release','reverse','simulation','solely','somewhat','submitted','successive','survive','thesis','topic','transmission','ultimately','unique','visible','voluntary','abandon','accompanied','accumulation','ambiguous','appendix','appreciation','arbitrary','automatically','bias','chart','clarity','conformity','commodity','complement','contemporary','contradiction','crucial','currency','denote','detected','deviation','displacement','dramatic','eventually','exhibit','exploitation','fluctuations','guidelines','highlighted','implicit','induced','inevitably','infrastructure','inspection','intensity','manipulation','minimised','nuclear','offset','paragraph','plus','practitioners','predominantly','prospect ','radical','random','reinforced','restore','revision','schedule','tension','termination','theme','thereby','uniform','vehicle','via','virtually','widespread','visual','accommodation','analogous','anticipated','assurance','attained','behalf','bulk','ceases','coherence','coincide','commenced','incompatible','concurrent','confined','controversy','conversely','device','devoted','diminished','distorted','duration','erosion','ethical','format','founded','inherent','insights','integral','intermediate','manual','mature','mediation','medium','military','minimal','mutual','norms','overlap','passive','portion','preliminary','protocol','qualitative','refine','relaxed ','restraints','revolution','rigid','route','scenario','sphere','subordinate','supplementary','suspended','team','temporary','trigger','unified','violation','vision ','adjacent','albeit','assembly','collapse','colleagues','compiled','conceived','convinced','depression','encountered','enormous','forthcoming','inclination','integrity','intrinsic','invoked','levy','likewise','nonetheless','notwithstanding','odd','ongoing','panel','persistent','posed','reluctant','so-called','straightforward','undergo','whereby']


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    '''opt1 = models.BooleanField(
        widget=widgets.CheckboxInput(),choices=['a','b','c']
    )'''
    final_tokens1=models.IntegerField(initial=0)
    final_tokens2 = models.IntegerField(initial=0)
    final_tokens3 = models.IntegerField(initial=0)
    final_tokens4 = models.IntegerField(initial=0)
    v1 = models.BooleanField(initial=False, blank=True)
    v2 = models.BooleanField(initial=False, blank=True)
    v3 = models.BooleanField(initial=False, blank=True)
    v4 = models.BooleanField(initial=False, blank=True)
    v5 = models.BooleanField(initial=False, blank=True)
    v6 = models.BooleanField(initial=False, blank=True)
    v7 = models.BooleanField(initial=False, blank=True)
    v8 = models.BooleanField(initial=False, blank=True)
    v9 = models.BooleanField(initial=False, blank=True)
    v10 = models.BooleanField(initial=False, blank=True)
    v11 = models.BooleanField(initial=False, blank=True)
    v12 = models.BooleanField(initial=False, blank=True)
    v13 = models.BooleanField(initial=False, blank=True)
    v14 = models.BooleanField(initial=False, blank=True)
    v15 = models.BooleanField(initial=False, blank=True)
    v16 = models.BooleanField(initial=False, blank=True)
    v17 = models.BooleanField(initial=False, blank=True)
    v18 = models.BooleanField(initial=False, blank=True)
    v19 = models.BooleanField(initial=False, blank=True)
    v20 = models.BooleanField(initial=False, blank=True)
    v21 = models.BooleanField(initial=False, blank=True)
    v22 = models.BooleanField(initial=False, blank=True)
    v23 = models.BooleanField(initial=False, blank=True)
    v24 = models.BooleanField(initial=False, blank=True)
    v25 = models.BooleanField(initial=False, blank=True)
    v26 = models.BooleanField(initial=False, blank=True)
    v27 = models.BooleanField(initial=False, blank=True)
    v28 = models.BooleanField(initial=False, blank=True)
    v29 = models.BooleanField(initial=False, blank=True)
    v30 = models.BooleanField(initial=False, blank=True)
    v31 = models.BooleanField(initial=False, blank=True)
    v32 = models.BooleanField(initial=False, blank=True)
    v33 = models.BooleanField(initial=False, blank=True)
    v34 = models.BooleanField(initial=False, blank=True)
    v35 = models.BooleanField(initial=False, blank=True)
    v36 = models.BooleanField(initial=False, blank=True)
    v37 = models.BooleanField(initial=False, blank=True)
    v38 = models.BooleanField(initial=False, blank=True)
    v39 = models.BooleanField(initial=False, blank=True)
    v40 = models.BooleanField(initial=False, blank=True)
    v41 = models.BooleanField(initial=False, blank=True)
    v42 = models.BooleanField(initial=False, blank=True)
    v43 = models.BooleanField(initial=False, blank=True)
    v44 = models.BooleanField(initial=False, blank=True)
    v45 = models.BooleanField(initial=False, blank=True)
    v46 = models.BooleanField(initial=False, blank=True)
    v47 = models.BooleanField(initial=False, blank=True)
    v48 = models.BooleanField(initial=False, blank=True)
    v49 = models.BooleanField(initial=False, blank=True)
    v50 = models.BooleanField(initial=False, blank=True)
    v51 = models.BooleanField(initial=False, blank=True)
    v52 = models.BooleanField(initial=False, blank=True)
    v53 = models.BooleanField(initial=False, blank=True)
    v54 = models.BooleanField(initial=False, blank=True)
    v55 = models.BooleanField(initial=False, blank=True)
    v56 = models.BooleanField(initial=False, blank=True)
    v57 = models.BooleanField(initial=False, blank=True)
    v58 = models.BooleanField(initial=False, blank=True)
    v59 = models.BooleanField(initial=False, blank=True)
    v60 = models.BooleanField(initial=False, blank=True)
    v61 = models.BooleanField(initial=False, blank=True)
    v62 = models.BooleanField(initial=False, blank=True)
    v63 = models.BooleanField(initial=False, blank=True)
    v64 = models.BooleanField(initial=False, blank=True)
    v65 = models.BooleanField(initial=False, blank=True)
    v66 = models.BooleanField(initial=False, blank=True)
    v67 = models.BooleanField(initial=False, blank=True)
    v68 = models.BooleanField(initial=False, blank=True)
    v69 = models.BooleanField(initial=False, blank=True)
    v70 = models.BooleanField(initial=False, blank=True)
    v71 = models.BooleanField(initial=False, blank=True)
    v72 = models.BooleanField(initial=False, blank=True)
    v73 = models.BooleanField(initial=False, blank=True)
    v74 = models.BooleanField(initial=False, blank=True)
    v75 = models.BooleanField(initial=False, blank=True)
    v76 = models.BooleanField(initial=False, blank=True)
    v77 = models.BooleanField(initial=False, blank=True)
    v78 = models.BooleanField(initial=False, blank=True)
    v79 = models.BooleanField(initial=False, blank=True)
    v80 = models.BooleanField(initial=False, blank=True)
    v81 = models.BooleanField(initial=False, blank=True)
    v82 = models.BooleanField(initial=False, blank=True)
    v83 = models.BooleanField(initial=False, blank=True)
    v84 = models.BooleanField(initial=False, blank=True)
    v85 = models.BooleanField(initial=False, blank=True)
    v86 = models.BooleanField(initial=False, blank=True)
    v87 = models.BooleanField(initial=False, blank=True)
    v88 = models.BooleanField(initial=False, blank=True)
    v89 = models.BooleanField(initial=False, blank=True)
    v90 = models.BooleanField(initial=False, blank=True)
    v91 = models.BooleanField(initial=False, blank=True)
    v92 = models.BooleanField(initial=False, blank=True)
    v93 = models.BooleanField(initial=False, blank=True)
    v94 = models.BooleanField(initial=False, blank=True)
    v95 = models.BooleanField(initial=False, blank=True)
    v96 = models.BooleanField(initial=False, blank=True)
    v97 = models.BooleanField(initial=False, blank=True)
    v98 = models.BooleanField(initial=False, blank=True)
    v99 = models.BooleanField(initial=False, blank=True)
    v100 = models.BooleanField(initial=False, blank=True)
    v101 = models.BooleanField(initial=False, blank=True)
    v102 = models.BooleanField(initial=False, blank=True)
    v103 = models.BooleanField(initial=False, blank=True)
    v104 = models.BooleanField(initial=False, blank=True)
    v105 = models.BooleanField(initial=False, blank=True)
    v106 = models.BooleanField(initial=False, blank=True)
    v107 = models.BooleanField(initial=False, blank=True)
    v108 = models.BooleanField(initial=False, blank=True)
    v109 = models.BooleanField(initial=False, blank=True)
    v110 = models.BooleanField(initial=False, blank=True)
    v111 = models.BooleanField(initial=False, blank=True)
    v112 = models.BooleanField(initial=False, blank=True)
    v113 = models.BooleanField(initial=False, blank=True)
    v114 = models.BooleanField(initial=False, blank=True)
    v115 = models.BooleanField(initial=False, blank=True)
    v116 = models.BooleanField(initial=False, blank=True)
    v117 = models.BooleanField(initial=False, blank=True)
    v118 = models.BooleanField(initial=False, blank=True)
    v119 = models.BooleanField(initial=False, blank=True)
    v120 = models.BooleanField(initial=False, blank=True)
    v121 = models.BooleanField(initial=False, blank=True)
    v122 = models.BooleanField(initial=False, blank=True)
    v123 = models.BooleanField(initial=False, blank=True)
    v124 = models.BooleanField(initial=False, blank=True)
    v125 = models.BooleanField(initial=False, blank=True)
    v126 = models.BooleanField(initial=False, blank=True)
    v127 = models.BooleanField(initial=False, blank=True)
    v128 = models.BooleanField(initial=False, blank=True)
    v129 = models.BooleanField(initial=False, blank=True)
    v130 = models.BooleanField(initial=False, blank=True)
    v131 = models.BooleanField(initial=False, blank=True)
    v132 = models.BooleanField(initial=False, blank=True)
    v133 = models.BooleanField(initial=False, blank=True)
    v134 = models.BooleanField(initial=False, blank=True)
    v135 = models.BooleanField(initial=False, blank=True)
    v136 = models.BooleanField(initial=False, blank=True)
    v137 = models.BooleanField(initial=False, blank=True)
    v138 = models.BooleanField(initial=False, blank=True)
    v139 = models.BooleanField(initial=False, blank=True)
    v140 = models.BooleanField(initial=False, blank=True)
    v141 = models.BooleanField(initial=False, blank=True)
    v142 = models.BooleanField(initial=False, blank=True)
    v143 = models.BooleanField(initial=False, blank=True)
    v144 = models.BooleanField(initial=False, blank=True)
    v145 = models.BooleanField(initial=False, blank=True)
    v146 = models.BooleanField(initial=False, blank=True)
    v147 = models.BooleanField(initial=False, blank=True)
    v148 = models.BooleanField(initial=False, blank=True)
    v149 = models.BooleanField(initial=False, blank=True)
    v150 = models.BooleanField(initial=False, blank=True)
    v151 = models.BooleanField(initial=False, blank=True)
    v152 = models.BooleanField(initial=False, blank=True)
    v153 = models.BooleanField(initial=False, blank=True)
    v154 = models.BooleanField(initial=False, blank=True)
    v155 = models.BooleanField(initial=False, blank=True)
    v156 = models.BooleanField(initial=False, blank=True)
    v157 = models.BooleanField(initial=False, blank=True)
    v158 = models.BooleanField(initial=False, blank=True)
    v159 = models.BooleanField(initial=False, blank=True)
    v160 = models.BooleanField(initial=False, blank=True)
    v161 = models.BooleanField(initial=False, blank=True)
    v162 = models.BooleanField(initial=False, blank=True)
    v163 = models.BooleanField(initial=False, blank=True)
    v164 = models.BooleanField(initial=False, blank=True)
    v165 = models.BooleanField(initial=False, blank=True)
    v166 = models.BooleanField(initial=False, blank=True)
    v167 = models.BooleanField(initial=False, blank=True)
    v168 = models.BooleanField(initial=False, blank=True)
    v169 = models.BooleanField(initial=False, blank=True)
    v170 = models.BooleanField(initial=False, blank=True)
    v171 = models.BooleanField(initial=False, blank=True)
    v172 = models.BooleanField(initial=False, blank=True)
    v173 = models.BooleanField(initial=False, blank=True)
    v174 = models.BooleanField(initial=False, blank=True)
    v175 = models.BooleanField(initial=False, blank=True)
    v176 = models.BooleanField(initial=False, blank=True)
    v177 = models.BooleanField(initial=False, blank=True)
    v178 = models.BooleanField(initial=False, blank=True)
    v179 = models.BooleanField(initial=False, blank=True)
    v180 = models.BooleanField(initial=False, blank=True)



# PAGES
class MyPage(Page):
    form_model = "player"
    #form_fields = ["number_entered"]
    timeout_seconds = 15

    @staticmethod
    def vars_for_template(player: Player):
        text = ''
        options = ['potential', 'appreciation', 'widespread', 'convinced', 'registered', 'impact', 'insert', 'removed', 'phase', 'environment', 'equipment', 'diversity', 'whereby', 'capacity', 'income']
        random.shuffle(options)
        #temp=['consequences', 'restraints', 'minimum', 'emerged', 'obvious', 'abandon', 'response', 'research', 'normal', 'scheme', 'simulation', 'mechanism', 'identical', 'dramatic', 'despite', 'author', 'journal', 'immigration', 'minorities', 'elements', 'logic', 'initial', 'apparent', 'investment', 'interaction', 'likewise', 'retained', 'crucial', 'psychology ', 'injury']
        #random.shuffle(sol)
        for i in options:
            text += i
            text += ' &nbsp '

        return {
            "text": text,
        }

class Form1(Page):
    form_model = 'player'
    form_fields = ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7','v8','v9','v10','v11','v12','v13','v14','v15','v16','v17','v18','v19','v20','v21', 'v22', 'v23','v24','v25','v26','v27','v28','v29','v30','v31','v32','v33','v34','v35','v36','v37','v38','v39','v40','v41','v42','v43','v44','v45']
    timeout_seconds = 45
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        #player.final_tokens=0
        if player.v1 == True:
            player.final_tokens1 += 1
        if player.v2 == True:
            player.final_tokens1 += 1
        if player.v4 == True:
            player.final_tokens1 += 1
        if player.v8 == True:
            player.final_tokens1 += 1
        if player.v16 == True:
            player.final_tokens1 += 1
        if player.v17 == True:
            player.final_tokens1 += 1
        if player.v19 == True:
            player.final_tokens1 += 1
        if player.v24 == True:
            player.final_tokens1 += 1
        if player.v25 == True:
            player.final_tokens1 += 1
        if player.v28 == True:
            player.final_tokens1 += 1
        if player.v31 == True:
            player.final_tokens1 += 1
        if player.v32 == True:
            player.final_tokens1 += 1
        if player.v35 == True:
            player.final_tokens1 += 1
        if player.v41 == True:
            player.final_tokens1 += 1
        if player.v42 == True:
            player.final_tokens1 += 1


class MyPage1(Page):
    form_model = "player"
    #form_fields = ["number_entered"]
    timeout_seconds = 15

    @staticmethod
    def vars_for_template(player: Player):
        text = ''
        options =['retained', 'intermediate', 'generation', 'manual', 'withstanding', 'ongoing', 'compounds', 'duration', 'highlighted', 'contemporary', 'furthermore', 'research', 'author', 'instance', 'portion']
        random.shuffle(options)
        #temp=['principle ', 'primary', 'file', 'abstract', 'generated', 'select', 'techniques', 'security', 'incentive', 'advocate', 'income', 'concept', 'sex', 'allocation', 'process', 'final', 'theme', 'access', 'contradiction', 'minorities', 'complex', 'hierarchical', 'function', 'equation', 'occupational', 'approximated', 'commodity', 'involved', 'global', 'dimensions']
        for i in options:
            text += i
            text += ' &nbsp '

        return {
            "text": text,
        }

class Form2(Page):
    form_model = 'player'
    form_fields = ['v46', 'v47', 'v48', 'v49', 'v50', 'v51', 'v52', 'v53', 'v54', 'v55', 'v56', 'v57', 'v58', 'v59', 'v60', 'v61', 'v62', 'v63', 'v64', 'v65', 'v66', 'v67', 'v68', 'v69', 'v70', 'v71', 'v72', 'v73', 'v74', 'v75', 'v76', 'v77', 'v78', 'v79', 'v80', 'v81', 'v82', 'v83', 'v84', 'v85', 'v86', 'v87', 'v88', 'v89', 'v90']
    timeout_seconds = 45
    @staticmethod
    #[1, 5, 6, 9, 13, 16, 20, 23, 25, 35, 38, 40, 43, 44]
    def before_next_page(player: Player, timeout_happened):

        if player.v46 == True:
            player.final_tokens2 += 1
        if player.v50 == True:
            player.final_tokens2 += 1
        if player.v51 == True:
            player.final_tokens2 += 1
        if player.v54 == True:
            player.final_tokens2 += 1
        if player.v58 == True:
            player.final_tokens2 += 1
        if player.v61 == True:
            player.final_tokens2 += 1
        if player.v65 == True:
            player.final_tokens2 += 1
        if player.v68 == True:
            player.final_tokens2 += 1
        if player.v70 == True:
            player.final_tokens2 += 1
        if player.v80 == True:
            player.final_tokens2 += 1
        if player.v83 == True:
            player.final_tokens2 += 1
        if player.v85 == True:
            player.final_tokens2 += 1
        if player.v88 == True:
            player.final_tokens2 += 1
        if player.v89 == True:
            player.final_tokens2 += 1


class MyPage2(Page):
    form_model = "player"
    #form_fields = ["number_entered"]
    timeout_seconds = 15

    @staticmethod
    def vars_for_template(player: Player):
        text = ''
        options = ['pursue', 'community', 'emerged', 'psychology ', 'diversity', 'colleagues', 'investigation', 'phase', 'assembly', 'hypothesis', 'final', 'achieve', 'marginal', 'termination', 'ethical']
        random.shuffle(options)
        #temp=['medical', 'revolution', 'authority', 'error', 'inherent', 'eliminate', 'insert', 'schedule', 'normal', 'transport', 'impact', 'stress', 'physical', 'contribution', 'clause', 'scope', 'inferred', 'chapter', 'devoted', 'involved', 'format', 'coordination', 'contrary', 'conference', 'annual', 'virtually', 'notion', 'contemporary', 'insights', 'academic']
        for i in options:
            text += i
            text += ' &nbsp '

        return {
            "text": text,
        }

class Form3(Page):
    form_model = 'player'
    form_fields = ['v91', 'v92', 'v93', 'v94', 'v95', 'v96', 'v97', 'v98', 'v99', 'v100', 'v101', 'v102', 'v103', 'v104', 'v105', 'v106', 'v107', 'v108', 'v109', 'v110', 'v111', 'v112', 'v113', 'v114', 'v115', 'v116', 'v117', 'v118', 'v119', 'v120', 'v121', 'v122', 'v123', 'v124', 'v125', 'v126', 'v127', 'v128', 'v129', 'v130', 'v131', 'v132', 'v133', 'v134', 'v135']
    timeout_seconds = 45
    @staticmethod
    def before_next_page(player: Player, timeout_happened):

        if player.v91 == True:
            player.final_tokens3 += 1
        if player.v92 == True:
            player.final_tokens3 += 1
        if player.v103 == True:
            player.final_tokens3 += 1
        if player.v104 == True:
            player.final_tokens3 += 1
        if player.v109 == True:
            player.final_tokens3 += 1
        if player.v113 == True:
            player.final_tokens3 += 1
        if player.v115 == True:
            player.final_tokens3 += 1
        if player.v117 == True:
            player.final_tokens3 += 1
        if player.v118 == True:
            player.final_tokens3 += 1
        if player.v119 == True:
            player.final_tokens3 += 1
        if player.v120 == True:
            player.final_tokens3 += 1
        if player.v122 == True:
            player.final_tokens3 += 1
        if player.v129 == True:
            player.final_tokens3 += 1
        if player.v131 == True:
            player.final_tokens3 += 1
        if player.v132 == True:
            player.final_tokens3 += 1


class MyPage3(Page):
    form_model = "player"
    #form_fields = ["number_entered"]
    timeout_seconds = 15

    @staticmethod
    def vars_for_template(player: Player):
        text = ''
        options = ['depression', 'media', 'specific', 'analogous', 'minorities', 'sufficient', 'mental', 'detected', 'paragraph', 'proportion', 'issues', 'integral', 'brief', 'incompatible', 'incentive']
        random.shuffle(options)
        #temp=['consequences', 'phenomenon', 'core', 'similar', 'cycle', 'benefit', 'survey', 'enhanced', 'required', 'interpretation', 'highlighted', 'cited', 'reluctant', 'restore', 'overlap', 'domain', 'exhibit', 'procedure', 'subordinate', 'technical', 'edition', 'deny', 'method', 'role', 'conflict', 'prime', 'equivalent', 'sustainable', 'validity', 'administration']
        for i in options:
            text += i
            text += ' &nbsp '

        return {
            "text": text,
        }

class Form4(Page):
    form_model = 'player'
    form_fields = ['v136', 'v137', 'v138', 'v139', 'v140', 'v141', 'v142', 'v143', 'v144', 'v145', 'v146', 'v147', 'v148', 'v149', 'v150', 'v151', 'v152', 'v153', 'v154', 'v155', 'v156', 'v157', 'v158', 'v159', 'v160', 'v161', 'v162', 'v163', 'v164', 'v165', 'v166', 'v167', 'v168', 'v169', 'v170', 'v171', 'v172', 'v173', 'v174', 'v175', 'v176', 'v177', 'v178', 'v179', 'v180']
    timeout_seconds = 45
    #[2, 3, 6, 8, 13, 15, 19, 28, 29, 33, 36, 37, 41, 43, 44]
    @staticmethod
    def before_next_page(player: Player, timeout_happened):

        if player.v137 == True:
            player.final_tokens4 += 1
        if player.v138 == True:
            player.final_tokens4 += 1
        if player.v141 == True:
            player.final_tokens4 += 1
        if player.v143 == True:
            player.final_tokens4 += 1
        if player.v148 == True:
            player.final_tokens4 += 1
        if player.v150 == True:
            player.final_tokens4 += 1
        if player.v154 == True:
            player.final_tokens4 += 1
        if player.v163 == True:
            player.final_tokens4 += 1
        if player.v164 == True:
            player.final_tokens4 += 1
        if player.v168 == True:
            player.final_tokens4 += 1
        if player.v171 == True:
            player.final_tokens4 += 1
        if player.v172 == True:
            player.final_tokens4 += 1
        if player.v176 == True:
            player.final_tokens4 += 1
        if player.v178 == True:
            player.final_tokens4 += 1
        if player.v179 == True:
            player.final_tokens4 += 1


class Direction(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    '''form_model = "player"
    @staticmethod
    def vars_for_template(player: Player):
        all_players = player.in_all_rounds()
        #player.final_tokens=0
        for temp in all_players:
            player.final_token=temp.final_tokens'''
    pass


page_sequence = [Direction, MyPage, Form1, MyPage1, Form2, MyPage2, Form3, MyPage3, Form4, Results]
