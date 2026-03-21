def seed(user_service, itinerary_service, user_model, itinerary_model, item_model):
    user = user_model("Daisy", "daisy@email.com")
    user_id = user_service.create_user(user)

    itin = itinerary_model(user_id, "Kerala Trip")
    itin_id = itinerary_service.create_itinerary(itin)

    itinerary_service.add_item(
        item_model(itin_id, "Beach", "Visit beach", "2026-03-25", "10:00", 500)
    )
    itinerary_service.add_item(
        item_model(itin_id, "Hotel", "Stay", "2026-03-26", "14:00", 2000)
    )

    return user_id, itin_id