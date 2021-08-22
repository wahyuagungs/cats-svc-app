from models.counterpart import Counterpart
from models.interface import Interface
from models.interface_item import InterfaceItem
from models.module import Module
from models.user import User

from exception.appexception import AppException
from exception.appexceptioncode import AppExceptionCode
from datetime import datetime
from utils import get_random_text
from models.base import db


def construct_database():
    """
    Initializes the database tables and relationships
    :return: None
    """
    db.create_all()
    db.session.commit()


def intialise_contents():
    """
    Initialise core contents into tables e.g. menus, roles
    :return: None
    """
    # fill the user
    admin_user = User(firstname="Admin", lastname="Admin",
                         email="wahyu.sugimartanto@pajak.go.id", username="admin",
                         is_activated=True)
    admin_user.password = "password"
    admin_user.activation_date = datetime.now()
    admin_user.activation_token = get_random_text(30)
    admin_user.organisation = "Administrator"
    commit([admin_user])

    # modules
    reg_module = Module('R', 'Registration', 'REG')
    crm_module = Module('AG', 'Compliance Risk Management', 'CRM')
    bi_module = Module('AH', 'Business Intelligence', 'BI')
    tam_module = Module('AI', 'Taxpayer Account Management', 'TAM')
    dqm_module = Module('AJ', 'Data Quality Management', 'DQM')
    dms_module = Module('AK', 'Document Management System', 'DMS')
    TS_module = Module('AL', 'Taxpayer Services', 'TS')
    Payment_module = Module('C', 'Payment', 'Payment')
    OA_module = Module('D', 'Objection and Appeal', 'OA')
    NO_module = Module('E', 'Non-Objection', 'NO')
    Exten_module = Module('F', 'Extensification', 'Exten')
    Supervisory_module = Module('G', 'Tax Supervisory', 'Supervisory')
    Audit_module = Module('I', 'Audit', 'Audit')
    CI_module = Module('K', 'Criminal Investigation', 'CI')
    Collection_module = Module('L', 'Collection', 'Collection')
    TRP_module = Module('M', 'Tax Return Processing', 'TRP')
    DPK_module = Module('N', 'Third Party Data Processing', 'DPK')
    OI_module = Module('O', 'Operational Intelligence', 'OI')
    Valuation_module = Module('U', 'Valuation', 'Valuation')
    EOI_module = Module('X.02', 'Exchange of Information', 'EOI')
    KM_module = Module('Y', 'Knowledge Management', 'KM')
    commit([reg_module, crm_module, bi_module, tam_module, dqm_module, dms_module,
            TS_module, Payment_module, OA_module, NO_module, Exten_module, Supervisory_module,
            Audit_module, CI_module, Collection_module, TRP_module, DPK_module, OI_module,
            Valuation_module, EOI_module, KM_module])

    # counterparts
    ilap_count = Counterpart('Instansi, Lembaga, Asosisi dan Pihak Lain (ILAP)', 'ILAP',
                             'Instansi, Lembaga, Asosisi dan Pihak Lain (ILAP)', 'ILAP')
    ksei_count = Counterpart('PT Kustodian Sentral Efek Indonesia', 'KSEI', 'PT Kustodian Sentral Efek Indonesia',
                             'KSEI')
    lk_count = Counterpart('Lembaga Keuangan', 'LK', 'Lembaga Keuangan', 'LK')
    pjap_count = Counterpart('Perusahaan Jasa Aplikasi Perpajakan (Application Service Provider)', 'PJAP',
                             'Perusahaan Jasa Aplikasi Perpajakan (Application Service Provider)', 'PJAP')
    psre_count = Counterpart('Penyelenggara Sertifikasi Elektronik (PSrE)', 'PSrE',
                             'Penyelenggara Sertifikasi Elektronik (PSrE)', 'PSrE')
    telco_count = Counterpart(
        'Telecommunication Providers (Telkomsel, XL Axiata, Indosat Ooredoo, Smartfren, Hutchison 3)', 'Telco',
        'Telecommunication Providers (Telkomsel, XL Axiata, Indosat Ooredoo, Smartfren, Hutchison 3)', 'Telco')
    bkpm_count = Counterpart('Badan Koordinasi Penanaman Modal', 'BKPM', 'Badan Koordinasi Penanaman Modal', 'BKPM')
    bpn_count = Counterpart('Badan Pertanahan Negara (Kementerian Agraria)', 'BPN',
                            'Badan Pertanahan Negara (Kementerian Agraria)', 'BPN')
    bsre_count = Counterpart('Balai Sertifikasi Elektronik (BSrE)', 'BSrE', 'Badan Siber dan Sandi Negara', 'BSSN')
    bank_count = Counterpart('Bank', 'Bank', 'Bank', 'Bank')
    bi_count = Counterpart('Bank Indonesia', 'BI', 'Bank Indonesia', 'BI')
    aem_count = Counterpart('DGT - AEM', 'AEM', 'Direktorat Jenderal Pajak', 'DJP')
    billing_core_v2_count = Counterpart('DGT - Legacy Billing Core', 'Billing_Core_v2', 'Direktorat Jenderal Pajak',
                                        'DJP')
    digital_map_count = Counterpart('DGT - Digital Map', 'Digital_Map', 'Direktorat Jenderal Pajak', 'DJP')
    portal_count = Counterpart('DGT - Portal ', 'Portal', 'Direktorat Jenderal Pajak', 'DJP')
    eform_count = Counterpart('DGT - CTAS', 'e-Form', 'Direktorat Jenderal Pajak', 'DJP')
    fax_count = Counterpart('DGT - Fax Server', 'Fax', 'Direktorat Jenderal Pajak', 'DJP')
    klip_count = Counterpart('DGT - Kantor Layanan Infiormasi dan Pengaduan', 'KLIP', 'Direktorat Jenderal Pajak',
                             'DJP')
    km_count = Counterpart('DGT - CTAS (Knowledge Management)', 'KM', 'Direktorat Jenderal Pajak', 'DJP')
    mail_server_count = Counterpart('DGT - Email Server', 'Mail_Server', 'Direktorat Jenderal Pajak', 'DJP')
    ppddp_count = Counterpart('DGT - Pusat Pengolahan Data dan Dokumen Perpajakan', 'PPDDP',
                              'Direktorat Jenderal Pajak', 'DJP')
    relawan_count = Counterpart('DGT - Aplikasi Relawan', 'Relawan', 'Direktorat Jenderal Pajak', 'DJP')
    sikka_count = Counterpart('DGT - HRIS/SIKKA', 'SIKKA', 'Direktorat Jenderal Pajak', 'DJP')
    sikop_count = Counterpart('DGT - SIKOP', 'SIKOP', 'Direktorat Jenderal Pajak', 'DJP')
    sisuka_count = Counterpart('DGT - Sistem Informasi Surat Keluar', 'SISUKA', 'Direktorat Jenderal Pajak', 'DJP')
    smaf_count = Counterpart('DGT - Sistem Manajemen Alat Forensik', 'SMAF', 'Direktorat Jenderal Pajak', 'DJP')
    tik_count = Counterpart('DGT - Direktorat Teknologi Informasi dan Komunikasi', 'TIK', 'Direktorat Jenderal Pajak',
                            'DJP')
    kejagung_count = Counterpart('Kejaksaaan Agung', 'Kejagung', 'Kejaksaaan Agung', 'Kejagung')
    dukcapil_count = Counterpart('Direktorat Jenderal Dukcapil', 'Dukcapil', 'Kementerian Dalam Negeri', 'Kemendagri')
    skk_migas_count = Counterpart('Satuan Kerja Khusus Pelaksana Kegiatan Usaha Hulu Minyak dan Gas Bumi.', 'SKK_MIGAS',
                                  'Kementerian ESDM', 'ESDM')
    ahu_count = Counterpart('Direktorat Jenderal Administrasi Hukum Umum', 'AHU',
                            'Kementerian Hukum dan Hak Asasi Manusia', 'Kemenkumham')
    imigrasi_count = Counterpart('Direktorat Jenderal Imigrasi', 'Imigrasi', 'Kementerian Hukum dan Hak Asasi Manusia',
                                 'Kemenkumham')
    pas_count = Counterpart('Direktorat Jenderal Pemasyarakatan', 'PAS', 'Kementerian Hukum dan Hak Asasi Manusia',
                            'Kemenkumham')
    bc_count = Counterpart('MoF - Direktorat Jenderal Bea Cukai', 'BC', 'Kementerian Keuangan', 'Kemenkeu')
    djkn_count = Counterpart('MoF - Direktorat Jenderal Kekayaan Negara', 'DJKN', 'Kementerian Keuangan', 'Kemenkeu')
    djpb_count = Counterpart('MoF - Direktorat Jenderal Perbendaharaan', 'DJPb', 'Kementerian Keuangan', 'Kemenkeu')
    djpk_count = Counterpart('MoF - Direktorat Jenderal Perimbangan Keuagan', 'DJPK', 'Kementerian Keuangan',
                             'Kemenkeu')
    insw_count = Counterpart('MoF - Indonesia National Single Window ', 'INSW', 'Kementerian Keuangan', 'Kemenkeu')
    p2pk_count = Counterpart('MoF - Pusat Pembinaan Profesi Keuangan (PPPK/P2PK)', 'P2PK', 'Kementerian Keuangan',
                             'Kemenkeu')
    pusintek_count = Counterpart('MoF - Pusat Informasi dan Teknologi Keuangan', 'Pusintek', 'Kementerian Keuangan',
                                 'Kemenkeu')
    setpp_count = Counterpart('MoF - Sekretariat Pengadilan Pajak', 'SETPP', 'Kementerian Keuangan', 'Kemenkeu')
    kemenlu_count = Counterpart('Kementerian Luar Negeri', 'Kemenlu', 'Kementerian Luar Negeri', 'Kemenlu')
    kemenpanrb_count = Counterpart('Kementerian Pendayagunaan Aparatur Negara dan Reformasi Birokrasi', 'KemenpanRB',
                                   'Kementerian Pendayagunaan Aparatur Negara dan Reformasi Birokrasi', 'KemenpanRB')
    hubla_count = Counterpart('Direktorat Jenderal Perhubungan Laut (Hubla)', 'HUBLA', 'Kementerian Perhubungan',
                              'Kemenhub')
    korlantas_count = Counterpart('Korps Lalu Lintas - Traffic Police Corps, National Police', 'Korlantas',
                                  'Kepolisian Republik Indonesia', 'Polri')
    pn_count = Counterpart('Pengadilan Niaga', 'PN', 'Mahkamah Agung', 'MA')
    cts_count = Counterpart('OECD', 'CTS', 'OECD', 'OECD')
    ojk_count = Counterpart('Otoritas Jasa Keuangan', 'OJK', 'Otoritas Jasa Keuangan', 'OJK')
    peruri_count = Counterpart('Perum Peruri (Percetakan Uang Republik Indonesia)', 'Peruri',
                               'Perum Peruri (Percetakan Uang Republik Indonesia)', 'Peruri')
    ppatk_count = Counterpart('Pusat Pelaporan dan Analisis Transaksi Keuangan', 'PPATK',
                              'Pusat Pelaporan dan Analisis Transaksi Keuangan', 'PPATK')
    anggaran_count = Counterpart('MoF - Direktorat Jenderal Anggaran', 'Anggaran', 'Kementerian Keuangan', 'Kemenkeu')
    existing_dms_count = Counterpart('DGT - Document Management System', 'Existing_DMS', 'Direktorat Jenderal Pajak',
                                     'DJP')
    commit([ilap_count, ksei_count, lk_count, pjap_count, psre_count, telco_count, bkpm_count,
            bpn_count, bsre_count, bank_count, bi_count, aem_count, billing_core_v2_count, digital_map_count,
            portal_count, eform_count, fax_count, klip_count, km_count, mail_server_count, ppddp_count,
            relawan_count, sikka_count, sikop_count, sisuka_count, smaf_count, tik_count, kejagung_count, dukcapil_count,
            skk_migas_count, ahu_count, imigrasi_count, pas_count, bc_count, djkn_count, djpb_count, djpk_count,
            insw_count, p2pk_count, pusintek_count, setpp_count, kemenlu_count, kemenpanrb_count, hubla_count, korlantas_count,
            pn_count, cts_count, ojk_count, peruri_count, anggaran_count, existing_dms_count, ppatk_count])


def commit(objs):
    for item in objs:
        db.session.add(item)
        db.session.commit()
