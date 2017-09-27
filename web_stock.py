"""Starting module for web application."""

from flask import Flask, render_template, request
from handle_exceptions import RequestError, data_form
from stocks_portfolio import (
    parse_form,
    get_final_frame
    )

app = Flask(__name__)


@app.errorhandler(RequestError)
def handle_invalid_usage(error):
    mess = error.get_data()
    return render_template(
           'error.html',
           message=mess
        )


@app.route('/foo')
def get_foo():
    raise RequestError(ValueError)


@app.route('/stocks', methods=['GET', 'POST'])
def stocks():
    """Maim function for calculate profil of stocks.
    Args:
        parse_form (string) parse data from form
        id_stocks (string) id by stocks
        result (DateFrame) table with handle stocks
        stock_close (list) closing price of each stock item
    """
    if request.method == 'GET':
        return render_template('form.html',
                               data_form=data_form)

    if request.method == 'POST':
        parse = parse_form(request.form["textcontent"])
        id_stocks = [item.stock_id for item in parse]
        result = get_final_frame(parse)
        print('DataFrame with all data\n', result)
        stock_close = [
            (
                id_stock,
                result[id_stock].tolist()
            )
            for id_stock in id_stocks]
        print(stock_close)

    return render_template(
            'stock.html',
            profit=result.total_profit.tolist(),
            revenue=result.total_revenue.tolist(),
            stock_close=stock_close,
            period=result.period.tolist(),
            data_form=request.form["textcontent"].split('\r\n')
            )


if __name__ == "__main__":
    app.run(debug=True)
