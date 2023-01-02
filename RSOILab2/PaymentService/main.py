from quart import Quart
from Payment.Models.ModelPayment import PaymentModel
from Payment.GetPayment import GetPaymentB
from Payment.PostPayment import PostPaymentB
from Payment.DeletePayment import DeletePaymentB
from Payment.Check import Check_B

app = Quart(__name__)
app.register_blueprint(GetPaymentB)
app.register_blueprint(PostPaymentB)
app.register_blueprint(DeletePaymentB)
app.register_blueprint(Check_B)


def create_tables():
    PaymentModel.drop_table()
    PaymentModel.create_table()


if __name__ == '__main__':
    create_tables()
    app.run(host='0.0.0.0',port=8050)