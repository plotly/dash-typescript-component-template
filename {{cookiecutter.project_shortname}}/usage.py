import {{cookiecutter.project_shortname}}
import dash

app = dash.Dash()

app.layout = {{cookiecutter.project_shortname}}.{{cookiecutter.component_name}}(id='component')


if __name__ == '__main__':
    app.run(debug=True)
