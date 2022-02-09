from otree.api import *
import random


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Wordlist'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 10
    #OPTIONS = ['analysis','approach','area','assessment','assume','authority','available','benefit','concept','consistent','constitutional','context','contract','create','data','definition','derived','distribution','economic','environment','established','estimate','evidence','export','factors','financial','formula','function','identified','income','indicate','individual','interpretation','involved','issues','labour','legal','legislation','major','method','occur','percent','period','policy','principle ','procedure','process','required','research','response','role','section','sector','significant','similar','source','specific','structure','theory','variables ','achieve','acquisition','administration','affect','appropriate','aspects','assistance','categories','chapter','commission','community','complex','computer','conclusion','conduct','consequences','construction','consumer','credit','cultural','design','distinction','elements','equation','evaluation','features','final','focus','impact','injury','institute','investment','items','journal','maintenance','normal','obtained','participation','perceived','positive','potential','previous','primary','purchase','range ','region','regulations','relevant','resident','resources','restricted','security','sought','select','site','strategies','survey','text','traditional','transfer','alternative','circumstances','comments','compensation','components','consent','considerable','constant','constraints','contribution','convention','coordination','core','corporate','corresponding','criteria','deduction','demonstrate','document','dominant','emphasis','ensure','excluded','framework','funds','illustrated','immigration','implies','initial','instance','interaction','justification','layer','link','location','maximum','minorities','negative','outcomes','partnership','philosophy','physical','proportion','published','reaction','registered','reliance','removed','scheme','sequence','sex','shift','specified','sufficient','task','technical','techniques','technology','validity','volume','access','adequate','annual','apparent','approximated','attitudes','attributed','civil','code','commitment','communication','concentration','conference','contrast','cycle','debate','despite','dimensions','domestic','emerged','error','ethnic','goals','granted','hence','hypothesis','implementation','implications','imposed','integration','internal','investigation','job','label','mechanism','obvious','occupational','option','output','overall','parallel','parameters','phase','predicted','principal','prior','professional','project','promote','regime','resolution','retained','series','statistics','status','stress','subsequent','sum','summary','undertaken','academic','adjustment','alter','amendment','aware','capacity','challenge','clause','compounds','conflict','consultation','contact','decline','discretion','draft','enable','energy','enforcement','entities','equivalent','evolution','expansion','exposure','external','facilitate','fundamental','generated','generation','image','liberal','licence','logic','marginal','medical','mental','modified','monitoring','network','notion','objective','orientation','perspective','precise','prime','psychology ','pursue','ratio','rejected','revenue','stability','styles','substitution','sustainable','symbolic','target','transition','trend','version','welfare','whereas ','abstract','accurate','acknowledged','aggregate','allocation','assigned','attached','author','bond','brief','capable','cited','cooperative','discrimination','display','diversity','domain','edition','enhanced','estate','exceed','expert','explicit','federal','fees','flexibility','furthermore','gender','ignored','incentive','incidence','incorporated','index','inhibition','initiatives','input','instructions','intelligence','interval','lecture','migration','minimum','ministry','motivation','neutral ','nevertheless','overseas','preceding','presumption','rational','recovery','revealed','scope','subsidiary','tapes','trace','transformation','transport','underlying','utility ','adaptation','adults','advocate','aid','channel','chemical','classical','comprehensive','comprise','confirmed','contrary','converted','couple','decades','definite','deny','differentiation','disposal','dynamic','eliminate','empirical','equipment','extract','file','finite','foundation','global','grade','guarantee','hierarchical','identical','ideology','inferred','innovation','insert','intervention','isolated','media','mode','paradigm','phenomenon','priority','prohibited','publication ','quotation','release','reverse','simulation','solely','somewhat','submitted','successive','survive','thesis','topic','transmission','ultimately','unique','visible','voluntary','abandon','accompanied','accumulation','ambiguous','appendix','appreciation','arbitrary','automatically','bias','chart','clarity','conformity','commodity','complement','contemporary','contradiction','crucial','currency','denote','detected','deviation','displacement','dramatic','eventually','exhibit','exploitation','fluctuations','guidelines','highlighted','implicit','induced','inevitably','infrastructure','inspection','intensity','manipulation','minimised','nuclear','offset','paragraph','plus','practitioners','predominantly','prospect ','radical','random','reinforced','restore','revision','schedule','tension','termination','theme','thereby','uniform','vehicle','via','virtually','widespread','visual','accommodation','analogous','anticipated','assurance','attained','behalf','bulk','ceases','coherence','coincide','commenced','incompatible','concurrent','confined','controversy','conversely','device','devoted','diminished','distorted','duration','erosion','ethical','format','founded','inherent','insights','integral','intermediate','manual','mature','mediation','medium','military','minimal','mutual','norms','overlap','passive','portion','preliminary','protocol','qualitative','refine','relaxed ','restraints','revolution','rigid','route','scenario','sphere','subordinate','supplementary','suspended','team','temporary','trigger','unified','violation','vision ','adjacent','albeit','assembly','collapse','colleagues','compiled','conceived','convinced','depression','encountered','enormous','forthcoming','inclination','integrity','intrinsic','invoked','levy','likewise','nonetheless','notwithstanding','odd','ongoing','panel','persistent','posed','reluctant','so-called','straightforward','undergo','whereby']


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    '''opt1 = models.BooleanField(
        widget=widgets.CheckboxInput(),choices=['a','b','c']
    )'''
    gender = models.StringField(
        choices=[['Male', 'Male'], ['Female', 'Female'], ['Others', 'Others'],
                 ['Don\'t want to say', 'Don\'t want to say']],
        label='What is your gender?',
        widget=widgets.RadioSelect(),
    )
    v1 = models.BooleanField(initial=False,blank=True)
    v2 = models.BooleanField(blank=True, initial=False)
    v3 = models.BooleanField(blank=True, initial=False)


# PAGES
class MyPage(Page):
    form_model = "player"
    #form_fields = ["number_entered"]
    timeout_seconds = 15

    @staticmethod
    def vars_for_template(player: Player):
        text = ''
        options = ['widespread', 'ideology', 'migration', 'commodity', 'apparent', 'initiatives', 'occupational', 'civil', 'generated', 'format', 'bulk', 'contemporary', 'investigation', 'tension', 'challenge']
        random.shuffle(options)
        #sol=['widespread', 'ideology', 'migration', 'commodity', 'apparent', 'initiatives', 'occupational', 'civil', 'generated', 'format', 'bulk', 'contemporary', 'investigation', 'tension', 'challenge','comprehensive', 'manipulation', 'conference', 'hierarchical', 'revealed', 'physical', 'protocol', 'factors', 'assume', 'violation', 'confirmed', 'considerable', 'acquisition', 'scheme', 'adjacent', 'strategies', 'label', 'goals', 'suspended', 'complement', 'marginal', 'source', 'innovation', 'visual', 'adequate']
        # random.shuffle(sol)
        for i in options:
            text += i
            text += ' &nbsp '

        return {
            "text": text,
        }

class Form1(Page):
    form_model = 'player'
    form_fields = ['v1', 'v2', 'v3']
    timeout_seconds = 45
    @staticmethod
    def before_next_page(player: Player, timeout_happened):

        if player.v1 == True:
            player.payoff = 123
        elif player.v2==True:
            player.payoff = 234



class MyPage1(Page):
    form_model = "player"
    #form_fields = ["number_entered"]
    timeout_seconds = 15

    @staticmethod
    def vars_for_template(player: Player):
        text = ''
        options = ['sector', 'categories', 'commitment', 'task', 'grade', 'licence', 'intermediate', 'evolution', 'plus', 'subordinate', 'conformity', 'route', 'extract', 'panel', 'prospect ']
        random.shuffle(options)
        #sol=['manipulation', 'conference', 'hierarchical', 'revealed', 'physical', 'protocol','sector', 'categories', 'commitment', 'task', 'grade', 'licence', 'intermediate', 'evolution', 'plus', 'subordinate', 'conformity', 'route', 'extract', 'panel', 'prospect','offset', 'initiatives', 'attitudes', 'focus', 'visual', 'practitioners', 'mutual', 'psychology ', 'transport', 'expansion', 'theme', 'minorities', 'federal', 'strategies', 'sum', 'exposure', 'furthermore', 'explicit', 'refine']
        #random.shuffle(sol)
        for i in options:
            text += i
            text += ' &nbsp '

        return {
            "text": text,
        }



class Direction(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Direction, MyPage, Form1,Results, MyPage1, ResultsWaitPage, Results]
