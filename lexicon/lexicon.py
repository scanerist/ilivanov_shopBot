from services import data_of_currency

LEXICON_RU: dict[str, str] = {
    '/start': 'Привет!\n'
              '<b>ilivanovshopbot</b> поможет тебе рассчитать сумму твоего заказа',
    'shoes': 'Рассчитать обувь💵',
    'Рассчитать обувь💵': f'Введите сумму в юанях для расчета стоимости\nактуальный курс: <b>{round(data_of_currency.current_for_one_CNY, 2)}</b>',
    'clothes': 'Рассчитать одежду, аксессуары💴',
    'Рассчитать одежду, аксессуары💴': f'Введите сумму в юанях для расчета стоимости\nактуальный курс: <b>{round(data_of_currency.current_for_one_CNY, 2)}</b>',
    'help': 'Часто задаваемые вопросы❗',
    'Часто задаваемые вопросы❗': 'Оформление заказа❗\n'
                                 'Для оформления заказа необходимо скинуть менеджеру скриншот и размер желаемой вещи с приложения DEWU\n\n'
                                 'Выкуп товара❗\n'
                                 'Выкуп товара происходит в день заказа! (Вам высылаются все необходимые скриншоты)\n\n'
                                 'Доставка❗\n'
                                 'Обычно доставка до СПб занимает 3-4 недели, в связи с различными праздниками сроки доставки могут быть увеличены\n\n'
                                 'Получение товара❗️\n'
                                 'Получить товар можно личной встречей СПб, отправка в регионы СДЭК, почта России',
    'feedback': 'Отзывы✉️',
    'Отзывы✉️': 'отзывы: https://vk.com/wall303473975_327',
    'other answer': 'я не понимаю че ты мне написал...',
    'error': 'не выбирай две команды одноврменно!'

}
