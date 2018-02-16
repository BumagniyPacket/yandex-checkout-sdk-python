import unittest

from yandex_checkout.domain.common.payment_method_type import PaymentMethodType
from yandex_checkout.domain.models.payment_data.card_type import CardType
from yandex_checkout.domain.models.payment_data.request.credit_card import CreditCard as RequestCreditCard
from yandex_checkout.domain.models.payment_data.request.payment_data_alfabank import \
    PaymentDataAlfabank as RequestPaymentDataAlfabank
from yandex_checkout.domain.models.payment_data.request.payment_data_applepay import \
    PaymentDataApplepay as RequestPaymentDataApplepay
from yandex_checkout.domain.models.payment_data.request.payment_data_cash import \
    PaymentDataCash as RequestPaymentDataCash
from yandex_checkout.domain.models.payment_data.request.payment_data_bank_card import \
    PaymentDataBankCard as RequestPaymentDataBankCard
from yandex_checkout.domain.models.payment_data.request.payment_data_mobile_balance import \
    PaymentDataMobileBalance as RequestPaymentDataMobileBalance
from yandex_checkout.domain.models.payment_data.request.payment_data_sberbank import \
    PaymentDataSberbank as RequestPaymentDataSberbank
from yandex_checkout.domain.models.payment_data.request.payment_data_qiwi import \
    PaymentDataQiwi as RequestPaymentDataQiwi
from yandex_checkout.domain.models.payment_data.response.credit_card import CreditCard as ResponseCreditCard
from yandex_checkout.domain.models.payment_data.response.payment_data_alfabank import \
    PaymentDataAlfabank as ResponsePaymentDataAlfabank
from yandex_checkout.domain.models.payment_data.response.payment_data_applepay import \
    PaymentDataApplepay as ResponsePaymentdataApplepay
from yandex_checkout.domain.models.payment_data.response.payment_data_cash import \
    PaymentDataCash as ResponsePaymentDataCash
from yandex_checkout.domain.models.payment_data.response.payment_data_bank_card import \
    PaymentDataBankCard as ResponsePaymentDataBankCard
from yandex_checkout.domain.models.payment_data.response.payment_data_mobile_balance import \
    PaymentDataMobileBalance as ResponsePaymentDataMobileBalance
from yandex_checkout.domain.models.payment_data.response.payment_data_sberbank import \
    PaymentDataSberbank as ResponsePaymentDataSberbank
from yandex_checkout.domain.models.payment_data.response.payment_data_qiwi import \
    PaymentDataQiwi as ResponsePaymentDataQiwi


class PaymentDataTest(unittest.TestCase):
    def test_alfabank_cast(self):
        payment_data = RequestPaymentDataAlfabank()
        payment_data.type = PaymentMethodType.ALFABANK
        payment_data.login = 'login'

        self.assertEqual({'type': PaymentMethodType.ALFABANK, 'login': 'login'}, dict(payment_data))

        payment_data = ResponsePaymentDataAlfabank()

        payment_data.type = PaymentMethodType.ALFABANK
        payment_data.login = 'login'

        self.assertEqual({'type': PaymentMethodType.ALFABANK, 'login': 'login'}, dict(payment_data))

    def test_bank_card_cast(self):
        payment_data = RequestPaymentDataBankCard()
        payment_data.type = PaymentMethodType.BANK_CARD
        payment_data.card = RequestCreditCard({
            'number': '8888888888880000',
            'expiry_year': '2018',
            'expiry_month': '10',
            'csc': '111',
            'cardholder': 'test'
        })

        self.assertEqual({'type': PaymentMethodType.BANK_CARD, 'card': {
            'number': '8888888888880000',
            'expiry_year': '2018',
            'expiry_month': '10',
            'csc': '111',
            'cardholder': 'test'
        }}, dict(payment_data))

        payment_data.card = {
            'number': '0000000000008888',
            'expiry_year': '2018',
            'expiry_month': '10',
            'csc': '111',
            'cardholder': 'test'
        }

        self.assertEqual({'type': PaymentMethodType.BANK_CARD, 'card': {
            'number': '0000000000008888',
            'expiry_year': '2018',
            'expiry_month': '10',
            'csc': '111',
            'cardholder': 'test'
        }}, dict(payment_data))

        with self.assertRaises(TypeError):
            payment_data.card = 'invalid type'

        payment_data = ResponsePaymentDataBankCard()
        payment_data.type = PaymentMethodType.BANK_CARD
        payment_data.card = ResponseCreditCard({
            'last4': '0000',
            'expiry_year': '2010',
            'expiry_month': '02',
            'card_type': CardType.VISA
        })

        self.assertEqual({'type': PaymentMethodType.BANK_CARD, 'card': {
            'last4': '0000',
            'expiry_year': '2010',
            'expiry_month': '02',
            'card_type': CardType.VISA
        }}, dict(payment_data))

        payment_data.card = {
            'last4': '0000',
            'expiry_year': '2010',
            'expiry_month': '02',
            'card_type': CardType.VISA
        }

        self.assertEqual({'type': PaymentMethodType.BANK_CARD, 'card': {
            'last4': '0000',
            'expiry_year': '2010',
            'expiry_month': '02',
            'card_type': CardType.VISA
        }}, dict(payment_data))

        with self.assertRaises(TypeError):
            payment_data.card = 'invalid type'

    def test_cash_cast(self):
        payment_data = RequestPaymentDataCash()
        payment_data.type = PaymentMethodType.CASH
        payment_data.phone = '799900000000'

        self.assertEqual({'type': PaymentMethodType.CASH, 'phone': '799900000000'}, dict(payment_data))

        with self.assertRaises(ValueError):
            payment_data.phone = 'invalid phone'

        payment_data = ResponsePaymentDataCash()
        payment_data.type = PaymentMethodType.CASH
        payment_data.phone = '799900000000'

        self.assertEqual({'type': PaymentMethodType.CASH, 'phone': '799900000000'}, dict(payment_data))

        with self.assertRaises(ValueError):
            payment_data.phone = 'invalid phone'

    def test_mobile_balance_cast(self):
        payment_data = RequestPaymentDataMobileBalance()
        payment_data.type = PaymentMethodType.MOBILE_BALANCE
        payment_data.phone = '799900000000'

        self.assertEqual({'type': PaymentMethodType.MOBILE_BALANCE, 'phone': '799900000000'}, dict(payment_data))

        with self.assertRaises(ValueError):
            payment_data.phone = 'invalid phone'

        payment_data = ResponsePaymentDataMobileBalance()
        payment_data.type = PaymentMethodType.MOBILE_BALANCE
        payment_data.phone = '799900000000'

        self.assertEqual({'type': PaymentMethodType.MOBILE_BALANCE, 'phone': '799900000000'}, dict(payment_data))

        with self.assertRaises(ValueError):
            payment_data.phone = 'invalid phone'

    def test_qiwi_cast(self):
        payment_data = RequestPaymentDataQiwi()
        payment_data.type = PaymentMethodType.QIWI
        payment_data.phone = '799900000000'

        self.assertEqual({'type': PaymentMethodType.QIWI, 'phone': '799900000000'}, dict(payment_data))

        with self.assertRaises(ValueError):
            payment_data.phone = 'invalid phone'

        payment_data = ResponsePaymentDataQiwi()
        payment_data.type = PaymentMethodType.QIWI
        payment_data.phone = '799900000000'

        self.assertEqual({'type': PaymentMethodType.QIWI, 'phone': '799900000000'}, dict(payment_data))

        with self.assertRaises(ValueError):
            payment_data.phone = 'invalid phone'

    def test_sberbank_cast(self):
        payment_data = RequestPaymentDataSberbank()
        payment_data.type = PaymentMethodType.SBERBANK
        payment_data.phone = '799900000000'

        self.assertEqual({'type': PaymentMethodType.SBERBANK, 'phone': '799900000000'}, dict(payment_data))

        with self.assertRaises(ValueError):
            payment_data.phone = 'invalid phone'

        payment_data = ResponsePaymentDataSberbank()
        payment_data.type = PaymentMethodType.SBERBANK
        payment_data.phone = '799900000000'

        self.assertEqual({'type': PaymentMethodType.SBERBANK, 'phone': '799900000000'}, dict(payment_data))

        with self.assertRaises(ValueError):
            payment_data.phone = 'invalid phone'

    def test_applepay_cast(self):
        payment_data = RequestPaymentDataApplepay()
        payment_data.payment_data = 'sampletoken'

        self.assertEqual({'type': PaymentMethodType.APPLEPAY, 'payment_data': 'sampletoken'}, dict(payment_data))

        payment_data = ResponsePaymentdataApplepay()
        payment_data.payment_data = 'sampletoken'

        self.assertEqual({'type': PaymentMethodType.APPLEPAY, 'payment_data': 'sampletoken'}, dict(payment_data))
