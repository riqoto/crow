import React, { useState } from 'react';

interface Method {
    name: string;
    signature: string;
    description: string;
    params?: string;
    returns?: string;
}

interface ClassAccordionProps {
    className: string;
    description: string;
    methods: Method[];
    attributes?: string[];
}

const ClassAccordion: React.FC<ClassAccordionProps> = ({
    className,
    description,
    methods,
    attributes,
}) => {
    const [isOpen, setIsOpen] = useState(false);

    return (
        <div className={`accordion ${isOpen ? 'accordion--open' : ''}`}>
            <div
                className="accordion__header"
                onClick={() => setIsOpen(!isOpen)}
                onKeyPress={(e) => e.key === 'Enter' && setIsOpen(!isOpen)}
                role="button"
                tabIndex={0}
            >
                <span className="accordion__title">
                    <code>{className}</code>
                </span>
                <span className="accordion__icon">
                    {isOpen ? '▼' : '▶'}
                </span>
            </div>

            <div className="accordion__content">
                <div className="class-info">
                    <p className="class-description">{description}</p>

                    {attributes && attributes.length > 0 && (
                        <div className="class-attributes">
                            <h4>Attributes</h4>
                            <ul>
                                {attributes.map((attr, index) => (
                                    <li key={index}>
                                        <code>{attr}</code>
                                    </li>
                                ))}
                            </ul>
                        </div>
                    )}

                    <div className="class-methods">
                        <h4>Methods</h4>
                        {methods.map((method, index) => (
                            <div key={index} className="method">
                                <div className="method__name">
                                    <code>{method.signature}</code>
                                </div>
                                <div className="method__description">
                                    {method.description}
                                </div>
                                {method.params && (
                                    <div className="method__section">
                                        <strong>Parameters:</strong>
                                        <div className="method__params">
                                            <code>{method.params}</code>
                                        </div>
                                    </div>
                                )}
                                {method.returns && (
                                    <div className="method__section">
                                        <strong>Returns:</strong>
                                        <div className="method__params">
                                            <code>{method.returns}</code>
                                        </div>
                                    </div>
                                )}
                            </div>
                        ))}
                    </div>
                </div>
            </div>
        </div>
    );
};

export default ClassAccordion;
