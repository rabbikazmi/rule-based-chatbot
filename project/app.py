from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Route to render the main HTML page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle chatbot messages
@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json.get('message', '').lower()

    # Simple rule-based responses
    if 'covid' in user_message or 'covid-19' in user_message:
        response = "COVID-19 vaccines are safe and effective. They help protect against severe illness, hospitalization, and death. Multiple doses may be recommended based on age and health status."
    elif 'side effects' in user_message:
        response = "Common vaccine side effects include: pain/swelling at the injection site, fatigue, headache, mild fever, muscle aches, and chills. These side effects usually resolve within a few days."
    elif 'schedule' in user_message or 'when' in user_message:
        response = "Vaccine schedules vary by type and age. Standard childhood vaccines follow a specific timeline, and adults may need certain boosters like flu shots, COVID-19 vaccines, and shingles shots."
    elif 'safety' in user_message:
        response = "Vaccines undergo extensive safety testing before approval. Clinical trials involving thousands of participants help ensure that vaccines are safe for the general population. Even after approval, vaccines are continuously monitored for safety."
    elif 'children' in user_message or 'kids' in user_message:
        response = "Children's vaccines protect against diseases like measles, mumps, rubella, polio, and more. The recommended schedule starts at birth and continues through adolescence."
    elif 'flu' in user_message or 'influenza' in user_message:
        response = "The flu vaccine is recommended for everyone 6 months and older. It is updated every year to match circulating strains of the virus. Getting the flu shot reduces the risk of severe illness and complications."
    elif 'pregnancy' in user_message or 'pregnant' in user_message:
        response = "Certain vaccines are safe and recommended during pregnancy, such as the flu vaccine and Tdap vaccine. It's important to consult your doctor to ensure you're up to date on the right vaccines for you during pregnancy."
    elif 'travel' in user_message or 'traveling' in user_message:
        response = "Travel vaccines depend on your destination. Common travel vaccines include Hepatitis A, Hepatitis B, Yellow Fever, Typhoid, and more. It's a good idea to visit a travel clinic 4-6 weeks before your trip."
    elif 'elderly' in user_message or 'seniors' in user_message:
        response = "Vaccination is particularly important for older adults. Seniors may need additional vaccines like the high-dose flu vaccine, pneumococcal vaccines, shingles vaccine, and COVID-19 boosters."
    elif 'cost' in user_message or 'price' in user_message or 'insurance' in user_message:
        response = "Many vaccines are covered by insurance, including private insurance, Medicare, and Medicaid. If you have no insurance, check with your local health department or clinics, which may offer vaccines at reduced cost or for free."
    elif 'how do vaccines work' in user_message or 'how do vaccines protect me' in user_message:
        response = "Vaccines work by stimulating your immune system to recognize and fight pathogens without causing the disease itself. They introduce a weakened or inactivated version of a virus or bacteria, or just a part of it, such as a protein, to help the body learn to respond."
    elif 'booster' in user_message or 'booster shot' in user_message:
        response = "Booster shots help maintain immunity against diseases, particularly for diseases like COVID-19, where immunity may decrease over time. The timing for boosters depends on the vaccine and your age."
    elif 'immunocompromised' in user_message or 'weak immune system' in user_message:
        response = "People with weakened immune systems may require additional or special vaccinations. It's important to consult a healthcare provider to get personalized vaccine recommendations."
    elif 'vaccine eligibility' in user_message or 'who can get vaccinated' in user_message:
        response = "Eligibility for vaccines varies depending on age, health status, and the type of vaccine. For COVID-19, vaccines are available to everyone aged 6 months and older, but the specific recommendations may vary based on local health guidelines."
    elif 'booster shot' in user_message:
        response = "A booster shot is an additional dose of a vaccine to enhance or restore immunity. For some vaccines, immunity may decrease over time, so a booster shot helps your body maintain protection against certain diseases."
    elif 'vaccine ingredients' in user_message:
        response = "Vaccines contain small amounts of ingredients to help the vaccine work effectively, such as antigens (to trigger immunity), adjuvants (to enhance the immune response), stabilizers, and preservatives. The ingredients vary depending on the vaccine."
    elif 'herd immunity' in user_message:
        response = "Herd immunity occurs when a large portion of a community becomes immune to a disease, making its spread less likely. Vaccines help achieve herd immunity by protecting individuals and preventing the spread of infectious diseases."
    elif 'autism' in user_message or 'link to autism' in user_message:
        response = "Extensive research has shown that there is no link between vaccines and autism. This myth was debunked by scientific studies, and vaccines are safe for children and adults."
    elif 'vaccine misinformation' in user_message:
        response = "There is a lot of misinformation about vaccines circulating online. It's important to rely on reputable sources like the CDC, WHO, or your healthcare provider for accurate information."
    elif 'hello' in user_message or 'hi' in user_message or 'hey' in user_message:
        response = "Hello! I'm your vaccine information assistant. How can I help you today? Feel free to ask about vaccine safety, schedules, side effects, or anything else!"
    else:
        response = "I can provide information about vaccines, including safety, schedules, side effects, and more. Please ask a specific question about vaccines!"

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
