CRYPTO_CATEGORY_NONE = 0
CRYPTO_CATEGORY_COIN = 1
CRYPTO_CATEGORY_TOKEN = 2


CATEGORIES_BY_NAME = {
    'coin': CRYPTO_CATEGORY_COIN,
    'token': CRYPTO_CATEGORY_TOKEN,
    'n/a': CRYPTO_CATEGORY_NONE
}

CATEGORIES_BY_CODE = {
    v: k for k, v in CATEGORIES_BY_NAME.items()
}


VALID_ASSET_FIELD_NAMES = [
    'symbol',
    'name',
    'asset_hash',
    'category',
    'logo',
    'description',
    'website',
]


CRYPTO_SYMBOLS = [
    'BTC',  # Bitcoin
    'ETH',  # Ethereum
    'XRP',  # XRP
    'LTC',  # Litecoin
    'EOS',  # EOS
    'BCH',  # Bitcoin Cash
    'BNB',  # Binance Coin
    'XLM',  # Stellar
    'USDT',  # Tether
    'TRX',  # TRON
    'ADA',  # Cardano
    'BSV',  # Bitcoin SV
    'XMR',  # Monero
    'MIOTA',  # IOTA
    'DASH',  # Dash
    'MKR',  # Maker
    'ONT',  # Ontology
    'NEO',  # NEO
    'ETC',  # Ethereum Classic
    'XTZ',  # Tezos
    'XEM',  # NEM
    'ZEC',  # Zcash
    'VET',  # VeChain
    'CRO',  # Crypto.com Chain
    'WAVES',  # Waves
    'BAT',  # Basic Attention Token
    'USDC',  # USD Coin
    'DOGE',  # Dogecoin
    'OMG',  # OmiseGO
    'QTUM',  # Qtum
    'BTG',  # Bitcoin Gold
    'TUSD',  # TrueUSD
    'DCR',  # Decred
    'LSK',  # Lisk
    'ZIL',  # Zilliqa
    'REP',  # Augur
    'DGB',  # DigiByte
    'RVN',  # Ravencoin
    'LINK',  # Chainlink
    'ZRX',  # 0x
    'HOT',  # Holo
    'ICX',  # ICON
    'STEEM',  # Steem
    'BTS',  # BitShares
    'ENJ',  # Enjin Coin
    'BCN',  # Bytecoin
    'BTT',  # BitTorrent
    'NANO',  # Nano
    'BCD',  # Bitcoin Diamond
    'HT',  # Huobi Token
    'AE',  # Aeternity
    'PAX',  # Paxos Standard Token
    'KMD',  # Komodo
    'XVG',  # Verge
    'MXM',  # Maximine Coin
    'BTM',  # Bytom
    'SC',  # Siacoin
    'NPXS',  # Pundi X
    'AOA',  # Aurora
    'IOST',  # IOST
    'THETA',  # THETA
    'KCS',  # KuCoin Shares
    'STRAT',  # Stratis
    'DAI',  # Dai
    'ABBC',  # ABBC Coin
    'PAI',  # Project Pai
    'SNT',  # Status
    'INB',  # Insight Chain
    'PPT',  # Populous
    'GNT',  # Golem
    'ARDR',  # Ardor
    'R',  # Revain
    'ARK',  # Ark
    'GXC',  # GXChain
    'REPO',  # REPO
    'CNX',  # Cryptonex
    'XIN',  # Mixin
    'GUSD',  # Gemini Dollar
    'HC',  # HyperCash
    'FCT',  # Factom
    'WAX',  # WAX
    'MAID',  # MaidSafeCoin
    'ETN',  # Electroneum
    'LOOM',  # Loom Network
    'QASH',  # QASH
    'DGTX',  # Digitex Futures
    'MANA',  # Decentraland
    'LRC',  # Loopring
    'MCO',  # Crypto.com
    'WTC',  # Waltonchain
    'QBIT',  # Qubitica
    'XZC',  # Zcoin
    'THR',  # ThoreCoin
    'ELF',  # aelf
    'PIVX',  # PIVX
    'WAN',  # Wanchain
    'MOAC',  # MOAC
    'NEXO',  # Nexo
    'KNC',  # Kyber Network
    'NAS',  # Nebulas
    'AION',  # Aion
    'POWR',  # Power Ledger
    'NULS',  # NULS
    'ELA',  # Elastos
    'ODE',  # ODEM
    'ETP',  # Metaverse ETP
    'DENT',  # Dent
    'ZEN',  # Horizen
    'BNT',  # Bancor
    'WICC',  # WaykiChain
    'RDD',  # ReddCoin
    'LKY',  # Linkey
    'STORJ',  # Storj
    'TOMO',  # TomoChain
    'DGD',  # DigixDAO
    'EURS',  # STASIS EURS
    'POLY',  # Polymath
    'GRS',  # Groestlcoin
    'QKC',  # QuarkChain
    'MONA',  # MonaCoin
    'BIX',  # Bibox Token
    'ENG',  # Enigma
    'SYS',  # Syscoin
    'TRUE',  # TrueChain
    'RLC',  # iExec RLC
    'VERI',  # Veritaseum
    'COSM',  # Cosmo Coin
    'PAY',  # TenX
    'SAN',  # Santiment Network Token
    'QNT',  # Quant
    'KIN',  # Kin
    'MHC',  # #MetaHash
    'NXT',  # Nxt
    'FUN',  # FunFair
    'GAS',  # Gas
    'META',  # Metadium
    'AGI',  # SingularityNET
    'CVC',  # Civic
    'LA',  # LATOKEN
    'GBYTE',  # Obyte
    'PZM',  # PRIZM
    'CMT',  # CyberMiles
    'TPAY',  # TokenPay
    'DAC',  # Davinci Coin
    'CTXC',  # Cortex
    'VTC',  # Vertcoin
    'NXS',  # Nexus
    'SLT',  # Smartlands
    'MITH',  # Mithril
    'APL',  # Apollo Currency
    'MFT',  # Mainframe
    'IOTX',  # IoTeX
    'BRD',  # Bread
    'MDA',  # Moeda Loyalty Points
    'ECOREAL',  # Ecoreal Estate
    'BCZERO',  # Buggyra Coin Zero
    'EDR',  # Endor Protocol
    'CND',  # Cindicator
    'DRGN',  # Dragonchain
    'RNT',  # OneRoot Network
    'NRG',  # Energi
    'GETX',  # Guaranteed Ethurance Token Extra
    'GBC',  # Gold Bits Coin
    'EDO',  # Eidoo
    'NEBL',  # Neblio
    'TCT',  # TokenClub
    'NET',  # NEXT
    'BZNT',  # Bezant
    'TTC',  # TTC Protocol
    'AUTO',  # Cube
    'PART',  # Particl
    'VEST',  # VestChain
    'GTO',  # Gifto
    'CENNZ',  # Centrality
    'UNO',  # Unobtanium
    'INO',  # INO COIN
    'ORME',  # Ormeus Coin
    'NEC',  # Nectar
    'ABT',  # Arcblock
    'S4F',  # S4FE
    'OCN',  # Odyssey
    'STORM',  # Storm
    'REQ',  # Request
    'C20',  # CRYPTO20
    'GO',  # GoChain
    'ROX',  # Robotina
    'TEL',  # Telcoin
    'CLAM',  # Clams
    'GVT',  # Genesis Vision
    'SCC',  # STEM CELL COIN
    'MAN',  # Matrix AI Network
    'CS',  # Credits
    'SRN',  # SIRIN LABS Token
    'RDN',  # Raiden Network Token
    'SMT',  # SmartMesh
    'MOC',  # Moss Coin
    'CWV',  # CWV Chain
    'PLC',  # PLATINCOIN
    'POE',  # Po.et
    'BFT',  # BnkToTheFuture
    'SMART',  # SmartCash
    'SXDT',  # Spectre.ai Dividend Token
    'BCV',  # BitCapitalVendor
    'CHX',  # Own
    'GNO',  # Gnosis
    'TKN',  # TokenCard
    'OST',  # OST
    'ETHOS',  # Ethos
    'NKN',  # NKN
    'ANT',  # Aragon
    'XPX',  # ProximaX
    'HPB',  # High Performance Blockchain
    'EMC2',  # Einsteinium
    'SKY',  # Skycoin
    'MTL',  # Metal
    'WGR',  # Wagerr
    'CVT',  # CyberVein
    'IGNIS',  # Ignis
    'IQ',  # Everipedia
    'GRIN',  # Grin
    'PRS',  # PressOne
    'XYO',  # XYO
    'MEDX',  # MediBloc [ERC20]
    'FSN',  # Fusion
    'HYC',  # HYCON
    'DCN',  # Dentacoin
    'CRPT',  # Crypterium
    'DATA',  # Streamr DATAcoin
    'EMC',  # Emercoin
    'WABI',  # Tael
    'MDS',  # MediShares
    'PPC',  # Peercoin
    'TKY',  # THEKEY
    'RUFF',  # Ruff
    'NAV',  # NavCoin
    'QSP',  # Quantstamp
    'B2G',  # Bitcoiin
    'SALT',  # SALT
    'LOC',  # LockTrip
    'REN',  # Ren
    'FTM',  # Fantom
    'EDG',  # Edgeless
    'DDD',  # Scry.info
    'CNUS',  # CoinUs
    'DMT',  # DMarket
    'BLOCK',  # Blocknet
    'HYN',  # Hyperion
    'MLN',  # Melon
    'BLZ',  # Bluzelle
    'VIA',  # Viacoin
    'RCN',  # Ripio Credit Network
    'UTK',  # UTRUST
    'MGO',  # MobileGo
    'VIBE',  # VIBE
    'KAN',  # BitKan
    'PRE',  # Presearch
    'PRG',  # Paragon
    'HUM',  # Humanscape
    'ICN',  # Iconomi
    'NOAH',  # Noah Coin
    'DROP',  # Dropil
    'NMC',  # Namecoin
    'DEW',  # DEW
    'ITC',  # IoT Chain
    'QRL',  # Quantum Resistant Ledger
    'PMA',  # PumaPay
    'PHX',  # Red Pulse Phoenix
    'BTU',  # BTU Protocol
    'VEE',  # BLOCKv
    'PEPECASH',  # Pepe Cash
    'APIS',  # APIS
    'SOLVE',  # SOLVE
    'NCASH',  # Nucleus Vision
    'ACT',  # Achain
    'LEO',  # LEOcoin
    'ADX',  # AdEx
    'XSN',  # Stakenet
    'DTA',  # DATA
    'TEN',  # Tokenomy
    'CVNT',  # Content Value Network
    'UBQ',  # Ubiq
    'NMR',  # Numeraire
    'SNGLS',  # SingularDTV
    'LAMB',  # Lambda
    'LEND',  # ETHLend
    'FLO',  # FLO
    'MED',  # MediBloc [QRC20]
    'XDN',  # DigitalNote
    'PBT',  # Primalbase Token
    'INS',  # Insolar
    'BOS',  # BOScoin
    'TRAC',  # OriginTrail
    'SBD',  # Steem Dollars
    'NLG',  # Gulden
    'QLC',  # QLC Chain
    'SDA',  # SDChain
    'DLT',  # Agrello
    'BCO',  # BridgeCoin
    'PRO',  # Propy
    'XAS',  # Asch
    'LBA',  # Cred
    'COSS',  # COSS
    'MOBI',  # Mobius
    'TERN',  # Ternio
    'MET',  # Metronome
    'TNB',  # Time New Bank
    'DNT',  # district0x
    'SNM',  # SONM
    'KEY',  # Selfkey
    'DBC',  # DeepBrain Chain
    'GTC',  # Game.com
    'SOC',  # All Sports
    'BURST',  # Burst
    'LRN',  # Loopring [NEO]
    'ZIP',  # Zipper
    'VITE',  # VITE
    'SCRL',  # SCRL
    'BEAM',  # Beam
    'AMB',  # Ambrosus
    'EVN',  # EvenCoin
    'PLR',  # Pillar
    'BBR',  # Boolberry
    'ECA',  # Electra
    'SUB',  # Substratum
    'RFR',  # Refereum
    'GOT',  # ParkinGo
    'ZRC',  # ZrCoin
    'TNT',  # Tierion
    'OIO',  # Online
    'CPC',  # CPChain
    'DBET',  # DecentBet
    'ARN',  # Aeron
    'TIOX',  # Trade Token X
    'APPC',  # AppCoins
    'UTNP',  # Universa
    'BTCP',  # Bitcoin Private
    'BITCNY',  # bitCNY
    'OSA',  # Optimal Shelf Availability Token
    'JNT',  # Jibrel Network
    'SNPC',  # SnapCoin
    'POA',  # POA Network
    'TUBE',  # BitTube
    'WPR',  # WePower
    'XWC',  # WhiteCoin
    'CSC',  # CasinoCoin
    'NIX',  # NIX
    'BAY',  # BitBay
    'MTC',  # doc.com Token
    'SPND',  # Spendcoin
    'GAME',  # GameCredits
    'BHPC',  # BHPCash
    'FREE',  # FREE Coin
    'FOAM',  # FOAM
    'EVR',  # Everus
    'BRZC',  # Breezecoin
    'FUEL',  # Etherparty
    'SAFEX',  # Safe Exchange Coin
    'VITAE',  # Vitae
    'RHOC',  # RChain
    'ZCL',  # ZClassic
    'PST',  # Primas
    'HYDRO',  # Hydro
    'EVX',  # Everex
    'DEC',  # Darico Ecosystem Coin
    'CNN',  # Content Neutrality Network
    'DX',  # DxChain Token
    'AC3',  # AC3
    'LYL',  # LoyalCoin
    'CZR',  # CanonChain
    'LCC',  # Litecoin Cash
    'LBC',  # LBRY Credits
    'NSD',  # Nasdacoin
    'IHT',  # IHT Real Estate Protocol
    'TRIO',  # Tripio
    'CPT',  # Cryptaur
    'BPT',  # Blockport
    'AST',  # AirSwap
    'DERO',  # Dero
    'MWAT',  # Restart Energy MWAT
    'DAPS',  # DAPS Token
    'SEELE',  # Seele
    'DEX',  # DEX
    'PLBT',  # Polybius
    'PASC',  # Pascal Coin
    'AMO',  # AMO Coin
    'LUN',  # Lunyr
    'MTH',  # Monetha
    'CDT',  # Blox
    'SLS',  # SaluS
    'INCNT',  # Incent
    'BLK',  # BlackCoin
    'AERGO',  # Aergo
    'YOYOW',  # YOYOW
    'USDS',  # StableUSD
    'CHSB',  # SwissBorg
    'MXC',  # Machine Xchange Coin
    'NPX',  # NaPoleonX
    'AU',  # AurumCoin
    'NEU',  # Neumark
    'AOG',  # smARTOFGIVING
    'PNT',  # Penta
    'QCH',  # QChi
    'LYM',  # Lympo
    'VEO',  # Amoveo
    'PPP',  # PayPie
    'SWM',  # Swarm
    'BITUSD',  # bitUSD
    'CAS',  # Cashaa
    'POLIS',  # Polis
    'STACS',  # STACS
    'MER',  # Mercury
    'BEET',  # Beetle Coin
    'MDT',  # Measurable Data Token
    'IOG',  # Playgroundz
    'GNX',  # Genaro Network
    'CLO',  # Callisto Network
    'COB',  # Cobinhood
    'LTO',  # LTO Network
    'NTK',  # Neurotoken
    'VIB',  # Viberate
    'KAT',  # Kambria
    'BCPT',  # BlockMason Credit Protocol
    'DOCK',  # Dock
    'LOKI',  # Loki
    'MGD',  # MassGrid
    'CAJ',  # Cajutel
    'INT',  # Internet Node Token
    'BTX',  # Bitcore
    'XCP',  # Counterparty
    'WWB',  # Wowbit
    'AMLT',  # AMLT
    'AEON',  # Aeon
    'UPP',  # Sentinel Protocol
    'EBC',  # EBCoin
    'BTO',  # Bottos
    'SSP',  # Smartshare
    'UKG',  # Unikoin Gold
    'WCT',  # Waves Community Token
    'IOC',  # I/O Coin
    'BZ',  # Bit-Z Token
    'BAAS',  # BaaSid
    'LINDA',  # Linda
    'CRYP',  # CrypticCoin
    'SHIFT',  # Shift
    'ECOM',  # Omnitude
    'SWFTC',  # SwftCoin
    'BAX',  # BABB
    'ADT',  # adToken
    'WINGS',  # Wings
    'AURA',  # Aurora DAO
    '$PAC',  # PACcoin
    'B2B',  # B2BX
    'XPM',  # Primecoin
    'DGX',  # Digix Gold Token
    'TMC',  # Timicoin
    'EOSDAC',  # eosDAC
    'PLY',  # PlayCoin [ERC20]
    'HLC',  # HalalChain
    'MRPH',  # Morpheus.Network
    'DCC',  # Distributed Credit Chain
    'ABL',  # Airbloc
    'PPY',  # Peerplays
    'COLX',  # ColossusXT
    'RBLX',  # Rublix
    'TFD',  # TE-FOOD
    'ONION',  # DeepOnion
    'MRK',  # MARK.SPACE
    'GCR',  # Global Currency Reserve
    'POT',  # PotCoin
    'DPY',  # Delphy
    'LML',  # Lisk Machine Learning
    'ZPT',  # Zeepin
    'QAC',  # Quasarcoin
    'NIM',  # Nimiq
    'GIN',  # GINcoin
    'HTML',  # HTMLCOIN
    'SENSE',  # Sense
    'SKM',  # Skrumble Network
    'UT',  # Ulord
    'SIX',  # SIX
    'GRFT',  # Graft
    'GEN',  # DAOstack
    'BWX',  # Blue Whale Token
    'OAX',  # OAX
    'CCCX',  # Clipper Coin
    'AVA',  # Travala.com
    'REM',  # Remme
    'ZCN',  # 0Chain
    'DIM',  # DIMCOIN
    'CBC',  # Cashbery Coin
    'XSPEC',  # Spectrecoin
    'BWT',  # Bittwatt
    'SPC',  # SpaceChain
    'INK',  # Ink
]
