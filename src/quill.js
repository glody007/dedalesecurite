import Quill from 'quill'

let Embed = Quill.import('blots/embed')

class DataBlot extends Embed {
  static create (value) {
    let node = super.create()
    node.setAttribute('src', value)
    node.innerHTML = `${value}`
    node.classList.add('data')
    return node
  }

  static value (node) {
    return node.getAttribute('src')
  }
}

DataBlot.blotName = 'data'
DataBlot.tagName = 'span'

class SecurisedBlot extends Embed {
  static create (value) {
    let node = super.create()
    node.setAttribute('src', value)
    node.innerHTML = `${value}`
    node.classList.add('securised')
    return node
  }

  static value (node) {
    return node.getAttribute('src')
  }
}

SecurisedBlot.blotName = 'securised'
SecurisedBlot.tagName = 'span'

Quill.register(DataBlot)
Quill.register(SecurisedBlot)

export default Quill
