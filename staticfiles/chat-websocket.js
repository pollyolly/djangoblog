const room_name = JSON.parse(document.getElementById('room-name').textContent); //Get RoomName value
var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws"
let url = ws_scheme+`://${window.location.host}/ws/djangoblog-socket/`+room_name+'/'

const chatSocket = new WebSocket(url)
chatSocket.onmessage = function(e){
        let data = JSON.parse(e.data)
        if(data.type == "chat"){
		console.log('Chat working');
                let messages = document.getElementById('chat-messages')
                messages.insertAdjacentHTML('beforeend',`
                        <div class="media">
                                <p class="float-right" style="float:right;margin-top:5px;"><small>${data.date}</small></p>
                                <div class="media-body">
                                        <h4 class="media-heading user_name">${data.name}</h4>
                                        ${data.message}
                                </div>
                        </div>
                        `)
		messages.scrollTop = messages.scrollHeight;

        }
}
let form = document.getElementById('chat-form')
form.addEventListener('submit', (e)=>{
        e.preventDefault()
        let chats = document.getElementById('chat-input')
        let name = document.getElementById('chat-name')
        let message = chats.value
        let chatter = name.value
        console.log(url)
        chatSocket.send(JSON.stringify({
                'type':"chat",
                'name':chatter,
                'message':message
        }))
        chats.value = ""
})
